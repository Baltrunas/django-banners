# -*- coding: utf-8 -*
from django.contrib import admin
from cms.models import *

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('display', 'slug', 'full_url', 'type', 'public')
	search_fields = ('display', 'slug', 'full_url', 'type', 'public')
	list_filter = ('type', 'public')
	list_editable = ('public',)
	class Media:
		js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textareas.js',)


admin.site.register(Category, CategoryAdmin)

class MetaTegInline(admin.TabularInline):
	model = MetaTeg
	extra = 0
		
class PagesAdmin(admin.ModelAdmin):
	list_display = ('title', 'url', 'full_url', '__unicode__', 'public')
	search_fields = ('title', 'url', 'full_url', 'public', 'text')
	list_filter = ('type', 'category')
	list_editable = ('public',)
	inlines = [MetaTegInline]
	class Media:
		js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textareas.js',)

admin.site.register(Pages, PagesAdmin)












# class TypeAdmin(admin.ModelAdmin):
	# list_display = ('name', 'slug', 'info')
	# search_fields = ('name', 'slug', 'info')

# admin.site.register(Type, TypeAdmin)