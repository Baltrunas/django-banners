# -*- coding: utf-8 -*
from django.shortcuts import redirect, get_object_or_404
from banners.models import Banner


def click(request, banner_id, key):
	banner = get_object_or_404(Banner, pk=banner_id)
	banner.log(request, 2, key)
	return redirect(banner.url)


def view(request, banner_id, key):
	banner = get_object_or_404(Banner, pk=banner_id)
	banner.log(request, 1, key)
	return redirect(banner.img.url)
