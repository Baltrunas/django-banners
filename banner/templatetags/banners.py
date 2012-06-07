# -*- coding: utf-8 -*
from django import template
from banner.models import Banner
register = template.Library()

@register.simple_tag(takes_context = True)
def banners(context, group, rotate, tpl):
	request = context['request']
	if rotate == 'one':
		result = Banner.objects.one()
		result.log(request, 0, result.key())
	elif rotate == 'time':
		result = Banner.objects.by_time()
		[one.log(request, 0, one.key()) for one in result]
	elif rotate == 'often':
		result = Banner.objects.by_often()
		[one.log(request, 0, one.key()) for one in result]
	elif rotate == 'all':
		result = Banner.objects.all()
		[one.log(request, 0, one.key()) for one in result]
	t = template.loader.get_template(tpl)
	return t.render( template.Context( {'banners': result, 'result': tpl} ) )