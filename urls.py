from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('banners.views',
    url(r'^click/(?P<banner_id>\d{1,4})/(?P<key>[-\w]+)/$', 'click', name='banner_click'),
    url(r'^view/(?P<banner_id>\d)/(?P<key>[-\w]+)/$', 'view', name='banner_view'),
)
