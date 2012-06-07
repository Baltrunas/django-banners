# -*- coding: utf-8 -*
from django.http import Http404
from django.conf import settings

from cms.models import *
from cms.views import page, category

from django.contrib.sites.models import Site

class PageMiddleware(object):
	def process_response(self, request, response):
		if response.status_code != 404:
			return response
		try:
			# categories = Category.objects.filter(public=True, full_url=request.path_info)
			# if categories:
				# return category(request, request.path_info)
			# pages = Pages.objects.filter(public=True, type='page', url=request.path_info),
			# if pages:
				# return page(request, request.path_info)
			return page(request, request.path_info)
		except Http404:
			return response
		except:
			if settings.DEBUG:
				raise
			return response

def SEO(request):
	return {
		'seo': Pages.objects.filter(public=True, type='SEO', url=request.path_info),
		'url': request.path_info,
		'site': Site.objects.get_current(),
	}