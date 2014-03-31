# -*- coding: utf-8 -*
from django.contrib import admin

from banners.models import URL
from banners.models import BannerGroup
from banners.models import Banner
from banners.models import Log

class URLAdmin(admin.ModelAdmin):
	list_display = ['title', 'url', 'regex', 'public', 'created_at', 'updated_at']
	search_fields = ['title', 'url', 'regex', 'sites', 'public', 'created_at', 'updated_at']
	list_filter = ['regex', 'sites', 'public']
	list_editable = ['regex', 'public']

admin.site.register(URL, URLAdmin)


class BannerAdminInline(admin.StackedInline):
	model = Banner
	extra = 1
	fields = ['public', 'title', 'url', 'img', 'often']


class BannerAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'url', 'sort', 'views', 'clicks', 'public', 'created_at', 'updated_at')
	search_fields = ('title', 'url', 'sort', 'views', 'clicks', 'public', 'created_at', 'updated_at')
	list_filter = ['public']
	list_editable = ['sort', 'public']

admin.site.register(Banner, BannerAdmin)


class BannerGroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'width', 'height', 'speed', 'public', 'created_at', 'updated_at')
	search_fields = ('name', 'slug', 'width', 'height', 'speed', 'public', 'created_at', 'updated_at')
	list_filter = ['public']
	list_editable = ['public']
	inlines = [BannerAdminInline]

admin.site.register(BannerGroup, BannerGroupAdmin)


class LogGroupAdmin(admin.ModelAdmin):
	list_display = ('banner', 'user', 'datetime', 'ip', 'user_agent', 'page', 'type')
	search_fields = ('banner', 'user', 'datetime', 'ip', 'user_agent', 'page', 'type', 'key')
	list_filter = ('type', 'banner', 'user', 'datetime', 'ip')

admin.site.register(Log, LogGroupAdmin)
