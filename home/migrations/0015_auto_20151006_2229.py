# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_imagepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('date', wagtail.wagtailcore.blocks.DateBlock()))),
        ),
    ]
