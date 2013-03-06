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
