from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
   (r'^$', 'views.index'),
   (r'^document/$', 'views.document'),
    # url(r'^default/', include('cms.urls')),

	url(r'^banner/', include('banner.urls')),
	

	
	
	url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^', include('cms.urls')),
)
