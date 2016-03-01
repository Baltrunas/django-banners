# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0003_auto_20151111_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='sites',
            field=models.ManyToManyField(related_name='site_urls', verbose_name='Sites', to='sites.Site', blank=True),
        ),
    ]
