from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^click/(?P<banner_id>\d{1,4})/(?P<key>[-\w]+)/$', views.click, name='banner_click'),
	url(r'^view/(?P<banner_id>\d+)/(?P<key>[-\w]+)/$', views.view, name='banner_view'),
]
