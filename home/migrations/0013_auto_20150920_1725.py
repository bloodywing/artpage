# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20150920_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagerelatedlink',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
