# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0003_auto_20150327_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail_model',
            name='back_picture',
            field=models.ImageField(null=True, upload_to=b'upload_images', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product_detail_model',
            name='front_picture',
            field=models.ImageField(null=True, upload_to=b'upload_images', blank=True),
            preserve_default=True,
        ),
    ]
