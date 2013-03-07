# -*- coding: utf-8 -*
from django import template
from banners.models import Banner
from banners.models import BannerGroup

register = template.Library()


@register.simple_tag(takes_context=True)
def banner_slider(context, group, tpl='slider.html'):
	try:
		group = BannerGroup.objects.get(slug=group)
		banners = Banner.objects.filter(group=group, public=True)
	except:
		banners = False
		group = False
	t = template.loader.get_template(tpl)
	return t.render(template.Context({'banners': banners, 'group': group}))


# block render
# # -*- utf-8 -*-
# from django.template import Context
# from django.template import Template

# from django import template
# register = template.Library()


# @register.simple_tag(takes_context=True)
# def render(context, content):
# 	try:
# 		tpl = Template(content)
# 		content = Context(context)
# 		return tpl.render(content)
# 	except:
# 		return 'Render Error'



# block area
# # -*- utf-8 -*-
# # import and register template library
# from django import template
# register = template.Library()

# # import models
# from blocks.models import Block
# from blocks.models import URL
# # import regex
# import re


# @register.simple_tag(takes_context=True)
# def blocks_area(context, area):
# 	request = context['request']

# 	blocks_area = []

# 	try:
# 		for url in URL.objects.all():
# 			if url.regex:
# 				url_re = re.compile(url.url)
# 				if url_re.findall(request.url):
# 					regex_urls_blocks = Block.objects.filter(public=True, sites=request.site, urls=url)
# 					blocks_area += regex_urls_blocks
# 			else:
# 				plain_urls_blocks = Block.objects.filter(public=True, sites=request.site, urls__url=request.url)
# 				blocks_area += plain_urls_blocks
# 		blocks_area_ids = [block.id for block in list(set(blocks_area))]
# 		blocks_area = Block.objects.filter(pk__in=blocks_area_ids).order_by('order')
# 	except:
# 		pass

# 	context['area'] = area
# 	context['blocks_area'] = blocks_area

# 	tpl = template.loader.get_template('blocks/area.html')
# 	return tpl.render(template.Context(context))






# block block
# # -*- utf-8 -*-
# # import and register template library
# from django import template
# register = template.Library()

# # import models
# from blocks.models import Block
# from blocks.models import URL
# # import regex
# import re


# @register.simple_tag(takes_context=True)
# def blocks_block(context, slug):
# 	request = context['request']

# 	block = False

# 	try:
# 		for url in URL.objects.all():
# 			if url.regex:
# 				url_re = re.compile(url.url)
# 				if url_re.findall(request.url):
# 					block = Block.objects.get(public=True, sites=request.site, urls=url, slug=slug)
# 			else:
# 				block = Block.objects.get(public=True, sites=request.site, urls__url=request.url, slug=slug)
# 	except:
# 		pass

# 	context['block'] = block

# 	tpl = template.loader.get_template('blocks/block.html')
# 	return tpl.render(template.Context(context))
