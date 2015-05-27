# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0002_auto_20150327_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first_page_model',
            name='image',
            field=models.ImageField(null=True, upload_to=b'upload_images', blank=True),
            preserve_default=True,
        ),
    ]
