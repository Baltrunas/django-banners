# -*- coding: utf-8 -*
from django.conf.urls import patterns, include, url

urlpatterns = patterns('cms.views',
	url(r'^$', 'category'),
	
		#	страница/
	#
	#	новости/
	#	новости/2000/
	#	новости/2000/04/
	#	новости/2000/04/30/
	#	новости/id100/
	#
	#	статьи/
	#	статьи/1/
	#	статьи/интересная-статья/
	#
	#	блог/
	#	блог/1/
	#	блог/интересная-статья/
	
	url(r'^(?P<full_url>\w+)/id(?P<id>\d+)/$', 'news_detail'),

	url(r'^(?P<full_url>[-\w]+)/(?P<year>\d{4})/$', 'news_year_archive'),
	url(r'^(?P<full_url>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/$', 'news_month_archive'),
	url(r'^(?P<full_url>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'news_day_archive'),
	
	url(r'^(?P<full_url>[-\D\w/_]+)/(?P<page>\d+)/$', 'category'),
	url(r'^(?P<full_url>[-\D\w/_]+)/$', 'category'),

	# url(r'^(?P<full_url>[-\w/_]+)/(\d+)/$', 'category'),
	
	# url(r'^news/(?P<id>[\d]+)/$', 'cms.views.news_detail', name='news_detail'),
	# url(r'^news/$', 'cms.views.news_list', name='news_list'),
	
	
	# url(r'^(?P<full_url>[-\w]+)/(?P<id>[\d]+)/$', 'cms.views.news_detail', name='news_detail'),

)
