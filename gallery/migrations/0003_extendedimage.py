# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
from django.conf import settings
import wagtail.wagtailimages.models
import wagtail.wagtailadmin.taggable


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0002_auto_20150918_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedImage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('file', models.ImageField(verbose_name='File', upload_to=wagtail.wagtailimages.models.get_upload_to, width_field='width', height_field='height')),
                ('width', models.IntegerField(editable=False, verbose_name='Width')),
                ('height', models.IntegerField(editable=False, verbose_name='Height')),
                ('created_at', models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='Created at')),
                ('focal_point_x', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_y', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_width', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_height', models.PositiveIntegerField(null=True, blank=True)),
                ('file_size', models.PositiveIntegerField(editable=False, null=True)),
                ('tags', taggit.managers.TaggableManager(help_text=None, to='taggit.Tag', verbose_name='Tags', through='taggit.TaggedItem', blank=True)),
                ('uploaded_by_user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, verbose_name='Uploaded by user', blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, wagtail.wagtailadmin.taggable.TagSearchable),
        ),
    ]
