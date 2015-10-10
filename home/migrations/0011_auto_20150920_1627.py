# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150920_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagerelatedlink',
            name='text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pagerelatedlink',
            name='image',
            field=models.ForeignKey(blank=True, related_name='+', to='gallery.ExtendedImage', null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
