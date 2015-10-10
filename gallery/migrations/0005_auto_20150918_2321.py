# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('gallery', '0004_extendedimage_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedRendition',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('file', models.ImageField(upload_to='images', height_field='height', width_field='width')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(editable=False, blank=True, default='', max_length=255)),
                ('filter', models.ForeignKey(related_name='+', to='wagtailimages.Filter')),
                ('image', models.ForeignKey(related_name='renditions', to='gallery.ExtendedImage')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='extendedrendition',
            unique_together=set([('image', 'filter', 'focal_point_key')]),
        ),
    ]
