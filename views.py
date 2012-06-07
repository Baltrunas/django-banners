# -*- coding: utf-8 -*
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import render_to_string
from cms.models import Pages

from banner.models import Banner
from files.models import FilesGroup, File

from django.template import RequestContext

from context import context

def index(request):
	page = get_object_or_404(Pages, url='index')
	context['page'] = page
	
	context['title'] = page.title
	context['header'] = page.header
	context['keywords'] = page.keywords
	context['description'] = page.description
	context['slider'] = Banner.objects.filter(public=True, group__slug='slider')
	return render_to_response('index.html', context, context_instance=RequestContext(request))

def document(request):
	context['title'] = 'Документы'
	context['header'] = 'Документы'
	context['keywords'] = 'Документы'
	context['description'] = 'Документы'
	context['files_group'] = FilesGroup.objects.get(type='doc')
	context['file_list'] = File.objects.filter(public=True, group__type='doc')
	return render_to_response('filelist.html', context, context_instance=RequestContext(request))