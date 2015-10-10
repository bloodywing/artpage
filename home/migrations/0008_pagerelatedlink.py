# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('home', '0007_simplepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageRelatedLink',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sort_order', models.IntegerField(null=True, blank=True, editable=False)),
                ('link_external', models.URLField(blank=True, verbose_name='External Link')),
                ('title', models.CharField(max_length=255, help_text='Link title')),
                ('link_page', models.ForeignKey(null=True, blank=True, related_name='+', to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(related_name='related_links', to='home.HomePage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
