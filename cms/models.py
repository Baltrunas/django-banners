# -*- coding: utf-8 -*
from django.db import models
from datetime import datetime

from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _
	
class Category(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	slug = models.SlugField(verbose_name=_('Slug'), unique=True)
	full_url = models.CharField(verbose_name=_('Full URL'), max_length=512, editable=False)
	parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, related_name='childs')
	
	TYPE_CHOICES = (
		('article', _('Article')),
		('blog', _('Blog')),
		('news', _('News')),
	)

	type = models.CharField(verbose_name=_('Type'), max_length=10, choices=TYPE_CHOICES)
	
	text = models.TextField(
		verbose_name=_('Text'),
		help_text='''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_text');">''' + _('ON \ OFF') + '</a> ' + _('Text'),
		blank=True
	)

	public = models.BooleanField(verbose_name=_('Public'), default=True)

	def full_url_puth (self, id):
		full_url_puth = Category.objects.get(pk=id).slug
		if not Category.objects.get(pk=id).parent:
			return full_url_puth
		else:
			return self.full_url_puth(Category.objects.get(pk=Category.objects.get(pk=id).parent.id).id) + '/' + full_url_puth

	def save(self, *args, **kwargs):
		super(Category, self).save(*args, **kwargs)
		self.full_url = self.full_url_puth(self.id)
		super(Category, self).save(*args, **kwargs)

	def display(self):
		space = ''
		url = self.full_url[1:len(self.full_url)-2]
		for x in url:
			if x == '/':
				space += '|___'
		return '<span style="color: #fff">%s</span>%s' % (space, self.name)
	display.short_description = _('Menu')
	display.allow_tags = True


	def __unicode__(self):
		space = ''
		url = self.full_url[1:len(self.full_url)-2]
		for x in url:
			if x == '/':
				space += '|___'
		return '%s%s' % (space, self.name)
	__unicode__.short_description = _('Menu')
	__unicode__.allow_tags = True

	class Meta:
		ordering = ['type', 'full_url', 'name']
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')

class Pages(models.Model):
	title = models.CharField(verbose_name=_('Title'), max_length=256)
	header = models.CharField(verbose_name=_('Header'), max_length=256)
	keywords = models.CharField(verbose_name=_('Keywords'), max_length=512)
	description = models.CharField(verbose_name=_('Description'), max_length=512)

	url = models.CharField(verbose_name=_('URL'), max_length=200, default='#')
	full_url = models.CharField(verbose_name=_('Full URL'), max_length=512, editable=False)

	TYPE_CHOICES = (
		('page', _('Page')),
		('article', _('Article')),
		('blog', _('Blog')),
		('news', _('News')),
		('seo', _('SEO')),
	)

	type = models.CharField(verbose_name=_('Type'), max_length=10, choices=TYPE_CHOICES)
	category = models.ForeignKey(Category, verbose_name=_('Categories'), blank=True, null=True, help_text=_('Archives, News and Blogs ONLY!'))

	intro_text = models.TextField(
		verbose_name=_('Intro Text'),
		help_text='''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_intro_text');">''' + _('ON \ OFF') + '</a> ' + _('Info'),
		blank=True,
		null=True
	)

	text = models.TextField(
		verbose_name=_('Text'),
		help_text='''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_text');">''' + _('ON \ OFF') + '</a> ' + _('Info'),
		blank=True,
		null=True
	)

	img = models.FileField(verbose_name=_('Image'), upload_to='img/pages', blank=True)
	
	site = models.ForeignKey(Site, verbose_name=_('Site'), null=True, blank=True)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	main = models.BooleanField(verbose_name=_('Main'), default=True)
	created = models.DateTimeField(verbose_name=_('Created'), default=datetime.now())
	updated = models.DateTimeField(verbose_name=_('Updated'), auto_now = True)

	views = models.PositiveIntegerField(verbose_name=_('Views'), editable=False, default=0)
	
	def save(self, *args, **kwargs):
		super(Pages, self).save(*args, **kwargs)
		if self.type == 'blog' or self.type == 'article':
			self.full_url = '/' + self.category.full_url + '/' + self.url + '/'
		else :
			self.full_url = self.url
		super(Pages, self).save(*args, **kwargs)

	
	def __unicode__(self):
		return self.title

	class Meta:
		unique_together = (('url', 'site'),)
		verbose_name = _('Page')
		verbose_name_plural = _('Pages')

class MetaTeg(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	value = models.CharField(verbose_name=_('Info'), max_length=1000, blank=True)
	pages = models.ForeignKey(Pages, verbose_name=_('Page'))

	def __unicode__(self):
		return self.name + ' = ' + self.value

	class Meta:
		ordering = ['name']
		verbose_name = _('MetaTeg')
		verbose_name_plural = _('MetaTegs')



# class Type(models.Model):
	# name = models.CharField(verbose_name=_('Name'), max_length=128)
	# slug = models.SlugField(verbose_name=_('Slug'))
	# info = models.TextField(
		# verbose_name=_('Info'),
		# help_text='''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_info');">''' + _('ON \ OFF') + '</a> ' + _('Info'),
		# blank=True,
		# null=True
	# )
	
	# def __unicode__(self):
		# return self.name

	# class Meta:
		# ordering = ['name']
		# verbose_name = _('Type')
		# verbose_name_plural = _('Types')