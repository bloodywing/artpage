# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_pagerelatedlink_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagerelatedlink',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', related_name='+', blank=True, null=True),
        ),
    ]
