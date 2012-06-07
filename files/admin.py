from django.contrib import admin
from files.models import File, FilesGroup

class FilesGroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'type', 'text')
	search_fields = ('name', 'type', 'text')

class FileAdmin(admin.ModelAdmin):
	list_display = ('name', 'file', 'public')
	search_fields = ('name', 'group', 'public')
	list_editable = ('public', )
	list_filter = ('group', 'public')


admin.site.register(FilesGroup, FilesGroupAdmin)
admin.site.register(File, FileAdmin)
