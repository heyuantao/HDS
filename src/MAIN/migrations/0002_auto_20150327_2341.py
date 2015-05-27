# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first_page_model',
            name='image',
            field=models.ImageField(upload_to=b'upload_images'),
            preserve_default=True,
        ),
    ]
