# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from context import context
from django.template import RequestContext

from datetime import datetime

from cms.models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def page(request, full_url):
	page = get_object_or_404(Pages, full_url=full_url)
	page.views += 1
	page.save()
	context['page'] = page
	context['title'] = page.title
	context['header'] = page.header
	context['keywords'] = page.keywords
	context['description'] = page.description
	if (page.type == 'article'):
		return render_to_response('article_detail.html', context, context_instance = RequestContext(request))
	elif (page.type == 'blog'):
		return render_to_response('blog_detail.html', context, context_instance = RequestContext(request))
	elif (page.type == 'news'):
		return render_to_response('news_detail.html', context, context_instance = RequestContext(request))
	else:
		return render_to_response('page_detail.html', context, context_instance = RequestContext(request))

def category(request, full_url, page=1):
	category = get_object_or_404(Category, full_url=full_url)
	context['category'] = category
	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	if (category.type == 'article'):
		return article_archive(request, full_url, page)
	elif (category.type == 'blog'):
		return blog_archive(request, full_url, page)
	elif (category.type == 'news'):
		return news_archive(request, full_url)

def article_archive(request, full_url, page=1):
	article_archive = Pages.objects.filter(public=True, type=context['category'].type, category=context['category'].id).order_by('-created')
	paginator = Paginator(article_archive, 4)
	try:
		article_archive = paginator.page(page)
	except PageNotAnInteger:
		article_archive = paginator.page(1)
	except EmptyPage:
		article_archive = paginator.page(1)
	context['article_archive'] = article_archive
	return render_to_response('article_archive.html', context, context_instance = RequestContext(request))

def blog_archive(request, full_url, page=1):
	blog_archive = Pages.objects.filter(public=True, type=context['category'].type, category=context['category'].id).order_by('-created')
	paginator = Paginator(blog_archive, 1)
	try:
		blog_archive = paginator.page(page)
	except PageNotAnInteger:
		blog_archive = paginator.page(1)
	except EmptyPage:
		blog_archive = paginator.page(1)
	context['blog_archive'] = blog_archive
	return render_to_response('blog_archive.html', context, context_instance = RequestContext(request))

def news_archive(request, full_url):
	year = datetime.now().year
	category = get_object_or_404(Category, full_url=full_url)
	context['news_year'] = year
	context['category'] = category
	
	context['news_archive'] = Pages.objects.filter(
		public=True,
		type=category.type,
		category=category.id,
	).order_by('-created')

	context['news_year_archive'] = Pages.objects.filter(
		public=True,
		type=category.type,
		category=category.id,
		created__year=year
	).order_by('-created')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('news_archive.html', context, context_instance = RequestContext(request))

def news_year_archive(request, full_url, year):
	category = get_object_or_404(Category, full_url=full_url)
	context['news_year'] = int(year)
	context['category'] = category
	
	context['news_archive'] = Pages.objects.filter(
		public=True,
		type=category.type,
		category=category.id,
	).order_by('-created')

	context['news_year_archive'] = Pages.objects.filter(
		public=True,
		type=category.type,
		category=category.id,
		created__year=year
	).order_by('-created')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('news_year_archive.html', context, context_instance = RequestContext(request))

def news_month_archive(request, full_url, year, month):
	category = get_object_or_404(Category, full_url=full_url)
	context['news_year'] = int(year)
	context['news_month'] = int(month)
	context['category'] = category
	
	context['news_archive'] = Pages.objects.filter(
		public=True,
		type=category.type,
		category=category.id,
	).order_by('-created')

	context['news_year_archive'] = Pages.objects.filter(
		public=True,
		type=category.type,
		category=category.id,
		created__year=year
	).order_by('-created')

	context['news_month_archive'] = Pages.objects.filter(
		public=True,
		type=category.type,
		category=category.id,
		created__year=year,
		created__month=month
	).order_by('-created')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('news_month_archive.html', context, context_instance = RequestContext(request))

def news_day_archive(request, full_url, year, month, day):
	category = get_object_or_404(Category, full_url=full_url)
	context['news_year'] = int(year)
	context['news_month'] = int(month)
	context['news_day'] = int(day)
	context['category'] = category
	
	context['news_archive'] = Pages.objects.filter(
		public=True,
		type=category.type,
		category=category.id,
	).order_by('-created')

	context['news_year_archive'] = Pages.objects.filter(
		public=True,
		type=category.type,
		category=category.id,
		created__year=year
	).order_by('-created')

	context['news_month_archive'] = Pages.objects.filter(
		public=True,
		type=category.type,
		category=category.id,
		created__year=year,
		created__month=month
	).order_by('-created')

	context['news_day_archive'] = Pages.objects.filter(
		public=True,
		type=category.type,
		category=category.id,
		created__year=year,
		created__month=month,
		created__day=day
	).order_by('-created')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('news_day_archive.html', context, context_instance = RequestContext(request))

def news_detail(request, full_url, id):
	category = get_object_or_404(Category, full_url=full_url)
	page = get_object_or_404(Pages, id=id, type='news', category=category.id)
	context['page'] = page
	context['title'] = page.title
	context['header'] = page.header
	context['keywords'] = page.keywords
	context['description'] = page.description
	return render_to_response('news_detail.html', context, context_instance = RequestContext(request))