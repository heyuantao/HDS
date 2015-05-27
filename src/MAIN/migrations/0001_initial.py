# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='first_page_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(max_length=255, upload_to=b'upload_images')),
                ('link_to', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': '\u56fe\u7247\u8bbe\u7f6e',
                'verbose_name_plural': '\u9996\u9875\u8bbe\u7f6e\uff08\u56fe\u7247\uff09',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='product_category_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '\u5206\u7c7b\u8be6\u60c5',
                'verbose_name_plural': '\u4ea7\u54c1\uff08\u6302\u9762\uff09\u6574\u4f53\u5206\u7c7b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='product_detail_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('net_content', models.IntegerField()),
                ('warranty_period', models.IntegerField()),
                ('nutritive_index', models.TextField(blank=True)),
                ('ingredient', models.TextField(blank=True)),
                ('preservation_method', models.TextField(blank=True)),
                ('front_picture', models.ImageField(max_length=255, upload_to=b'upload_images')),
                ('back_picture', models.ImageField(max_length=255, upload_to=b'upload_images')),
                ('display_on_first_page', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='MAIN.product_category_model')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u4fe1\u606f',
                'verbose_name_plural': '\u4ea7\u54c1\uff08\u6302\u9762\uff09\u8be6\u60c5\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='product_picture_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('info1_picture', models.ImageField(max_length=255, upload_to=b'upload_images')),
                ('info2_picture', models.ImageField(max_length=255, upload_to=b'upload_images')),
                ('info3_picture', models.ImageField(max_length=255, upload_to=b'upload_images')),
            ],
            options={
                'verbose_name': '\u56fe\u7247\u8bbe\u7f6e',
                'verbose_name_plural': '\u4ea7\u54c1\uff08\u6302\u9762\uff09\u5e7f\u544a\u56fe\u7247',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='site_info_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=50)),
                ('value', models.TextField()),
                ('picture', models.ImageField(max_length=255, upload_to=b'upload_images')),
            ],
            options={
                'verbose_name': '\u8bbe\u7f6e',
                'verbose_name_plural': '\u7ad9\u70b9\u4e13\u6709\u6570\u636e\u8bbe\u7f6e',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product_detail_model',
            name='product_pic',
            field=models.ForeignKey(to='MAIN.product_picture_model'),
            preserve_default=True,
        ),
    ]
