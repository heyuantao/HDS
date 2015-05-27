# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WX', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ResponseByKeywordsModel',
            new_name='Response_By_Keywords_Model',
        ),
    ]
