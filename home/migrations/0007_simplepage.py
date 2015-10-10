# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('home', '0006_sociallabel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simplepage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, to='wagtailcore.Page', auto_created=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
