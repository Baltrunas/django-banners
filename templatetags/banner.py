import re

from django import template

from ..models import Banner
from ..models import BannerGroup
from ..models import URL


register = template.Library()


@register.simple_tag(takes_context=True)
def banner_group(context, group, tpl='banners/group.html'):
	try:
		page_url = context['request'].path_info
		site = context['request'].site
		group = BannerGroup.objects.get(slug=group)
		good_urls = []
		for url in URL.objects.filter(public=True, sites__in=[site]):
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
	if(banners and group):
		context['banners'] = banners
		context['group'] = group

	t = template.loader.get_template(tpl)
	return t.render(template.Context(context))
