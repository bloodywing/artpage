# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20150918_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedimage',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
