# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0004_auto_20150329_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_picture_model',
            name='info1_picture',
            field=models.ImageField(upload_to=b'upload_images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product_picture_model',
            name='info2_picture',
            field=models.ImageField(upload_to=b'upload_images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product_picture_model',
            name='info3_picture',
            field=models.ImageField(upload_to=b'upload_images'),
            preserve_default=True,
        ),
    ]
