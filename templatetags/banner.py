# -*- coding: utf-8 -*
from banners.models import Banner
from banners.models import BannerGroup
from banners.models import URL

from django import template

# For render tag
# from django.template import Context
# from django.template import Template

import re

register = template.Library()


@register.simple_tag(takes_context=True)
def banner_group(context, group, tpl='slider.html'):
	try:
		request = context['request']
		group = BannerGroup.objects.get(slug=group)

		good_urls = []
		for url in URL.objects.filter(public=True):
			if url.regex:
				url_re = re.compile(url.url)
				if url_re.findall(request.url):
					good_urls.append(url)
			elif request.url == url.url:
				good_urls.append(url)

		banners = Banner.objects.filter(public=True, group=group, urls__in=good_urls)
	except:
		banners = False
		group = False

	t = template.loader.get_template(tpl)
	return t.render(template.Context({'banners': banners, 'group': group}))


@register.simple_tag(takes_context=True)
def banner_one(context, banner_id, tpl='banner.html'):
	try:
		request = context['request']

		good_urls = []
		for url in URL.objects.filter(public=True):
			if url.regex:
				url_re = re.compile(url.url)
				if url_re.findall(request.url):
					good_urls.append(url)
			elif request.url == url.url:
				good_urls.append(url)

		banner = Banner.objects.get(id=banner_id, public=True, urls__in=good_urls)
	except:
		banner = False

	t = template.loader.get_template(tpl)
	return t.render(template.Context({'banner': banner}))


# block render
@register.simple_tag(takes_context=True)
def render(context, content):
	try:
		tpl = Template(content)
		content = Context(context)
		return tpl.render(content)
	except:
		return 'Render Error'
