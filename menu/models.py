# -*- coding: utf-8 -*
from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _

class MenuGroup(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	type = models.SlugField(verbose_name=_('Type'), max_length=128)
	text = models.TextField(
		verbose_name=_('Text'),
		help_text='''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_text');">''' + _('ON \ OFF') + '</a> ' + _('Text')
	)

	def menu(self):
		return '<a href="/admin/menu/menu/?group__id__exact=%s"><img src="%sprefs_16.png"></a>' % (self.id, str(settings.STATIC_URL))

	menu.short_description = _('Menu')
	menu.allow_tags = True

	def count(self):
		return Menu.objects.filter(group=self.id).count()
	count.short_description = _('Count')
	
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _('Menu Group')
		verbose_name_plural = _('Menus Groups')

class Menu(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	url = models.CharField(verbose_name=_('URL'), max_length=255, default='#')
	order = models.SlugField(verbose_name=_('Order'), max_length=512, editable=False)
	group = models.ForeignKey(MenuGroup, verbose_name=_('Menu Group'))
	parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, related_name='childs')
	icon = models.ImageField(verbose_name=_('Icon'), upload_to='img/menu', blank=True)

	text = models.TextField(
		verbose_name=_('Text'),
		help_text='''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_text');">''' + _('ON \ OFF') + '</a> ' + _('Text'),
		blank=True
	)
	sort = models.PositiveSmallIntegerField(verbose_name=_('Sort'), default=500)
	public = models.BooleanField(verbose_name=_('Public'), default=True)

	def icon_preview(self):
		if self.icon:
			return '<img src="%s">' % self.icon.url
		else:
			return '(none)'
	icon_preview.short_description = _('Icon')
	icon_preview.allow_tags = True


	def order_puth (self, id):
		order_puth = Menu.objects.get(pk=id).name
		if not Menu.objects.get(pk=id).parent:
			return 'order_puth'
		else:
			return self.order_puth(Menu.objects.get(pk=Menu.objects.get(pk=id).parent.id).id) + '|' + order_puth

	def save(self, *args, **kwargs):
		super(Menu, self).save(*args, **kwargs)
		self.order = self.order_puth(self.id)
		super(Menu, self).save(*args, **kwargs)
	
	def delete(self):
		super(Menu, self).delete()

	def display(self):
		space = ''
		for x in self.order:
			if x == '|':
				space += '|___'
		return '<span style="color: #fff">%s</span>%s' % (space, self.name)
	display.short_description = _('Menu')
	display.allow_tags = True


	def __unicode__(self):
		space = ''
		for x in self.order:
			if x == '|':
				space += '|___'
		return '%s%s' % (space, self.name)
	__unicode__.short_description = _('Menu')
	__unicode__.allow_tags = True

	class Meta:
		ordering = ['order', 'sort', 'name']
		verbose_name = _('Menu')
		verbose_name_plural = _('Menus')