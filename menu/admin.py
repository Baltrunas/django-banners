# -*- coding: utf-8 -*
from django.contrib import admin
from menu.models import *

class MenuGroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'type', 'text', 'menu', 'count')
	search_fields = ('name', 'type', 'text', 'id')
	# class Media:
		# js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textareas.js',)

class MenuAdmin(admin.ModelAdmin):
	list_display = ('display', 'url', 'group', 'sort', 'public', 'icon_preview')
	search_fields = ('name', 'url', 'group', 'sort', 'public')
	list_editable = ('public', 'sort')
	list_filter = ('group', 'public')
	class Media:
		js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textareas.js',)

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuGroup, MenuGroupAdmin)
