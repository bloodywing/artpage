# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_socialwidget_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='main_image',
            field=models.ForeignKey(blank=True, null=True, to='gallery.ExtendedImage', related_name='+', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
