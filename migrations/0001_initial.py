# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('alt', models.CharField(max_length=255, verbose_name='Alt')),
                ('text', models.TextField(null=True, verbose_name='Text', blank=True)),
                ('img', models.FileField(upload_to=b'banners', null=True, verbose_name='Image', blank=True)),
                ('url', models.CharField(max_length=1024, verbose_name='URL')),
                ('sort', models.PositiveSmallIntegerField(default=500, verbose_name='Sort')),
                ('often', models.PositiveSmallIntegerField(help_text='A ten will display 10 times more often that a one.', verbose_name='Often', choices=[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]])),
                ('html', models.BooleanField(default=False, verbose_name='Is HTML?')),
                ('flash', models.BooleanField(default=False, verbose_name='Is Flash?')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'ordering': ['sort'],
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='BannerGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('width', models.PositiveSmallIntegerField(default=0, verbose_name='Width')),
                ('height', models.PositiveSmallIntegerField(default=0, verbose_name='Height')),
                ('speed', models.PositiveSmallIntegerField(default=2000, verbose_name='Speed')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Banner Group',
                'verbose_name_plural': 'Banner Groups',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Clicked At')),
                ('ip', models.IPAddressField(null=True, verbose_name='IP', blank=True)),
                ('user_agent', models.CharField(max_length=1024, null=True, verbose_name='User Agent', blank=True)),
                ('page', models.URLField(null=True, verbose_name='Page', blank=True)),
                ('key', models.CharField(max_length=32, null=True, verbose_name='User Agent', blank=True)),
                ('type', models.PositiveSmallIntegerField(default=0, max_length=1, verbose_name='Type', choices=[(0, b'impressions'), (1, b'view'), (2, b'click')])),
                ('banner', models.ForeignKey(related_name='banner_logs', to='banners.Banner')),
                ('group', models.ForeignKey(related_name='group_logs', verbose_name='Group', blank=True, to='banners.BannerGroup')),
            ],
        ),
        migrations.CreateModel(
            name='LogStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Data')),
                ('view', models.PositiveIntegerField(verbose_name='Views')),
                ('click', models.PositiveIntegerField(verbose_name='Clicks')),
                ('unique_click', models.PositiveIntegerField(null=True, verbose_name='Unique Views', blank=True)),
                ('unique_view', models.PositiveIntegerField(verbose_name='Unique Clicks')),
                ('banner', models.ForeignKey(related_name='banner_stat', verbose_name='Banner', blank=True, to='banners.Banner')),
                ('group', models.ForeignKey(related_name='group_stat', verbose_name='Group', blank=True, to='banners.BannerGroup')),
            ],
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('url', models.CharField(max_length=2048, verbose_name='URL or URL RegEx')),
                ('regex', models.BooleanField(default=False, verbose_name='RegEx')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('sites', models.ManyToManyField(related_name='site_urls', null=True, verbose_name='Sites', to='sites.Site', blank=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
            },
        ),
        migrations.AddField(
            model_name='logstat',
            name='urls',
            field=models.ManyToManyField(related_name='url_bloks', null=True, verbose_name='URLs', to='banners.URL', blank=True),
        ),
        migrations.AddField(
            model_name='log',
            name='urls',
            field=models.ManyToManyField(related_name='url_logs', verbose_name='URLs', to='banners.URL', blank=True),
        ),
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(related_name='users', verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='group',
            field=models.ForeignKey(related_name='banners', verbose_name='Group', to='banners.BannerGroup'),
        ),
        migrations.AddField(
            model_name='banner',
            name='urls',
            field=models.ManyToManyField(related_name='url_banners', null=True, verbose_name='URLs', to='banners.URL', blank=True),
        ),
    ]
