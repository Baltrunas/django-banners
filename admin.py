from django.contrib import admin

from .models import URL
from .models import BannerGroup
from .models import Banner

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
	list_display = ['__str__', 'url', 'sort', 'public', 'created_at', 'updated_at']
	search_fields = ['title', 'url', 'sort', 'public', 'created_at', 'updated_at']
	list_filter = ['public']
	list_editable = ['sort', 'public']

admin.site.register(Banner, BannerAdmin)


class BannerGroupAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'size', 'speed', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'slug', 'size', 'speed', 'public', 'created_at', 'updated_at']
	list_filter = ['public']
	list_editable = ['public']
	inlines = [BannerAdminInline]

admin.site.register(BannerGroup, BannerGroupAdmin)
