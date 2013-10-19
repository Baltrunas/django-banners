# -*- coding: utf-8 -*
from banners.models import Banner
from banners.models import BannerGroup
from banners.models import URL

from django import template

# For render tag
from django.template import Context
from django.template import Template

import re

register = template.Library()


@register.simple_tag(takes_context=True)
def banner_group(context, group, tpl='group.html'):
	try:
		page_url = context['request'].META['QUERY_STRING']
		group = BannerGroup.objects.get(slug=group)
		good_urls = []
		for url in URL.objects.filter(public=True):
			if url.regex:
				url_re = re.compile(url.url)
				if url_re.findall(page_url):
					good_urls.append(url)
			elif page_url == url.url:
				good_urls.append(url)

		banners = Banner.objects.filter(public=True, group=group, urls__in=good_urls)
	except:
		banners = False
		group = False

	context['banners'] = banners
	context['group'] = group

	t = template.loader.get_template(tpl)
	return t.render(template.Context(context))


@register.simple_tag(takes_context=True)
def banner_one(context, banner_id, tpl='banner.html'):
	try:
		page_url = context['request'].META['QUERY_STRING']
		good_urls = []
		for url in URL.objects.filter(public=True):
			if url.regex:
				url_re = re.compile(url.url)
				if url_re.findall(page_url):
					good_urls.append(url)
			elif page_url == url.url:
				good_urls.append(url)

		banner = Banner.objects.get(id=banner_id, public=True, urls__in=good_urls)
	except:
		banner = False

	context['banner'] = banner

	t = template.loader.get_template(tpl)
	return t.render(template.Context(context))


# block render
@register.simple_tag(takes_context=True)
def render(context, content):
	try:
		tpl = Template(content)
		content = Context(context)
		return tpl.render(content)
	except:
		return 'Render Error'
