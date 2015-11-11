# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0002_auto_20151111_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='flash',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='html',
        ),
        migrations.AddField(
            model_name='banner',
            name='file_type',
            field=models.CharField(default=b'image', max_length=32, verbose_name='URL', choices=[(b'image', 'Image'), (b'flash', 'Flash'), (b'html', 'HTML')]),
        ),
    ]
