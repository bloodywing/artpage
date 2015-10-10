# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('wagtailredirects', '0002_add_verbose_names'),
        ('wagtailforms', '0002_add_verbose_names'),
        ('blog', '0004_blogindexpage_blogindexrelatedlink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindex',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='BlogIndex',
        ),
    ]
