import hashlib
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.sites.models import Site

from .managers import BiasedManager


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

	title = models.CharField(verbose_name=_('Title'), max_length=255, blank=True)
	alt = models.CharField(verbose_name=_('Alt'), max_length=255)

	text = models.TextField(verbose_name=_('Text'), blank=True, null=True)
	img = models.FileField(verbose_name=_('Image'), upload_to='banners', blank=True, null=True)
	url = models.CharField(verbose_name=_('URL'), max_length=1024)

	sort = models.PositiveSmallIntegerField(verbose_name=_('Sort'), default=500)

	group = models.ForeignKey(BannerGroup, related_name='banners', verbose_name=_('Group'))
	often = models.PositiveSmallIntegerField(
		verbose_name=_('Often'),
		help_text=_('A ten will display 10 times more often that a one.'),
		choices=[[i, i] for i in range(11)]
	)
	urls = models.ManyToManyField(URL, related_name='url_banners', verbose_name=_('URLs'), null=True, blank=True)


	FILE_TYPE_CHICES = (
		('image', _('Image')),
		('flash', _('Flash')),
		('html', _('HTML')),
	)
	file_type = models.CharField(verbose_name=_('URL'), max_length=32, choices=FILE_TYPE_CHICES, default='image')

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.title or self.alt

	class Meta:
		ordering = ['sort']
		verbose_name = _('Banner')
		verbose_name_plural = _('Banners')
