# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_pagerelatedlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagerelatedlink',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
