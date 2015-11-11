# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='log',
            name='group',
        ),
        migrations.RemoveField(
            model_name='log',
            name='urls',
        ),
        migrations.RemoveField(
            model_name='log',
            name='user',
        ),
        migrations.RemoveField(
            model_name='logstat',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='logstat',
            name='group',
        ),
        migrations.RemoveField(
            model_name='logstat',
            name='urls',
        ),
        migrations.DeleteModel(
            name='Log',
        ),
        migrations.DeleteModel(
            name='LogStat',
        ),
    ]
