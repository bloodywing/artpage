# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20151007_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialwidget',
            name='html',
            field=models.TextField(blank=True),
        ),
    ]
