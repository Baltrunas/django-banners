from django.db import models
from django.utils.translation import ugettext as _
class FilesGroup(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	type = models.SlugField(verbose_name=_('Type'), max_length=128)
	text = models.TextField(
		verbose_name=_('Text'),
		help_text='''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_text');">''' + _('ON \ OFF') + '</a> ' + _('Text')
	)
	
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _('Files Group')
		verbose_name_plural = _('Files Groups')

class File(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	group = models.ForeignKey(FilesGroup, verbose_name=_('Files Group'), related_name='files')
	file = models.FileField(upload_to='dl-files', max_length=200)
	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=0)
	download = models.PositiveSmallIntegerField(verbose_name=_('Download'), default=0, editable=False)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)
	class Meta:
		ordering = ['name']
	