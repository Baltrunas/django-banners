# -*- coding: utf-8 -*
from django.db import models
from django.utils.translation import ugettext_lazy as _
from banners.managers import BiasedManager
from django.conf import settings
from django.contrib.sites.models import Site

import hashlib
from datetime import datetime


class URL(models.Model):
	title = models.CharField(verbose_name=_('Title'), max_length=256)
	url = models.CharField(verbose_name=_('URL or URL RegEx'), max_length=2048)
	regex = models.BooleanField(verbose_name=_('RegEx'), default=False)
	sites = models.ManyToManyField(Site, related_name='site_urls', verbose_name=_('Sites'), null=True, blank=True)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-created_at']
		verbose_name = _('URL')
		verbose_name_plural = _('URLs')


class BannerGroup (models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	slug = models.SlugField(verbose_name=_('Slug'), unique=True)
	width = models.PositiveSmallIntegerField(verbose_name=_('Width'), default=0)
	height = models.PositiveSmallIntegerField(verbose_name=_('Height'), default=0)
	speed = models.PositiveSmallIntegerField(verbose_name=_('Speed'), default=2000)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def size(self):
		return '%sx%s' % (self.width, self.height)

	def __unicode__(self):
		return '%s - [%s x %s]' % (self.name,  self.width, self.height)

	class Meta:
		ordering = ['name']
		verbose_name = _('Banner Group')
		verbose_name_plural = _('Banner Groups')


class Banner(models.Model):
	objects = BiasedManager()

	title = models.CharField(verbose_name=_('Title'), max_length=255)
	alt = models.CharField(verbose_name=_('Alt'), max_length=255)

	text = models.TextField(verbose_name=_('Text'), blank=True, null=True)
	img = models.FileField(verbose_name=_('Image'), upload_to='banners')
	url = models.CharField(verbose_name=_('URL'), max_length=1024)
	group = models.ForeignKey(BannerGroup, related_name='banners', verbose_name=_('Group'))
	often = models.PositiveSmallIntegerField(
		verbose_name=_('Often'),
		help_text=_('A ten will display 10 times more often that a one.'),
		choices=[[i, i] for i in range(11)]
	)
	urls = models.ManyToManyField(URL, related_name='url_banners', verbose_name=_('URLs'), null=True, blank=True)

	hrml = models.BooleanField(verbose_name=_('Is HTML?'), default=False)
	flash = models.BooleanField(verbose_name=_('Is HTML?'), default=False)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def key(slef):
		if hasattr(settings, 'SECRET_KEY'):
			key = str(datetime.now()) + settings.SECRET_KEY
		else:
			key = str(datetime.now())
		return hashlib.md5(key).hexdigest()

	def log(self, request, type, key):
		log = {
			'type': type,
			'key': key,
			'banner': self,
			'ip': request.META.get('REMOTE_ADDR'),
			'user_agent': request.META.get('HTTP_USER_AGENT'),
			'page': request.META.get('HTTP_REFERER'),
		}

		if request.user.is_authenticated():
			log['user'] = request.user
		return Log.objects.create(**log)

	@models.permalink
	def image(self):
		return ('banner_view', (), {'banner_id': self.pk, 'key': self.key()})

	def impressions(self):
		return Log.objects.filter(banner=self.pk, type=0).count()

	def views(self):
		return Log.objects.filter(banner=self.pk, type=1).count()

	def clicks(self):
		return Log.objects.filter(banner=self.pk, type=2).count()

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		if self.url == '#':
			return self.url
		else:
			@models.permalink
			def get_absolute_url(self):
				return ('banner_click', (), {'banner_id': self.pk, 'key': self.key()})
			return get_absolute_url(self)


class Log(models.Model):
	banner = models.ForeignKey(Banner, related_name='banner_logs')
	group = models.ForeignKey(BannerGroup, related_name='group_logs', verbose_name=_('Group'), blank=True)
	urls = models.ManyToManyField(URL, related_name='url_logs', verbose_name=_('URLs'), blank=True)

	user = models.ForeignKey('auth.User', null=True, blank=True, related_name='users', verbose_name=_('User'))
	datetime = models.DateTimeField(verbose_name=_('Clicked At'), auto_now_add=True)
	ip = models.IPAddressField(verbose_name=_('IP'), null=True, blank=True)
	user_agent = models.CharField(verbose_name=_('User Agent'), max_length=1024, null=True, blank=True)
	page = models.URLField(verbose_name=_('Page'), null=True, blank=True)
	key = models.CharField(verbose_name=_('User Agent'), max_length=32, null=True, blank=True)
	TYPE_CHOICES = (
		(0, 'impressions'),
		(1, 'view'),
		(2, 'click')
	)

	type = models.PositiveSmallIntegerField(verbose_name=_('Type'), max_length=1, default=0, choices=TYPE_CHOICES)

	def __unicode__(self):
		return '%s - (%s)' % (self.banner, self.datetime)


class LogStat(models.Model):
	banner = models.ForeignKey(Banner, related_name='banner_stat', verbose_name=_('Banner'), blank=True)
	group = models.ForeignKey(BannerGroup, related_name='group_stat', verbose_name=_('Group'), blank=True)
	urls = models.ManyToManyField(URL, related_name='url_bloks', verbose_name=_('URLs'), null=True, blank=True)

	date = models.DateField(verbose_name=_('Data'))
	view = models.PositiveIntegerField(verbose_name=_('Views'))
	click = models.PositiveIntegerField(verbose_name=_('Clicks'))
	unique_click = models.PositiveIntegerField(verbose_name=_('Unique Views'), blank=True, null=True)
	unique_view = models.PositiveIntegerField(verbose_name=_('Unique Clicks'))

	def __unicode__(self):
		return '%s - (%s)' % (self.banner, self.date)
