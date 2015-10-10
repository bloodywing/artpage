# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_extendedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedimage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
