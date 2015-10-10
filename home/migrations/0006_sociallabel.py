# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20150919_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLabel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.URLField(null=True)),
                ('color', models.CharField(max_length=6, help_text='Color in HTML Color Code, HEX: #xxxxxx')),
                ('text', models.CharField(blank=True, null=True, max_length=255)),
                ('icon', models.CharField(blank=True, null=True, help_text='Fontawesome Iconname eg: facebook, twitter, instagram', max_length=50)),
            ],
        ),
    ]
