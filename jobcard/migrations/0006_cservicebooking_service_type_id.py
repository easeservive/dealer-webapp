# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcard', '0005_auto_20170919_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='cservicebooking',
            name='service_type_id',
            field=models.CharField(default='5s5d5f5g', max_length=20),
            preserve_default=False,
        ),
    ]