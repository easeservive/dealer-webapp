# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcard', '0002_auto_20170912_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cservicebooking',
            name='booking_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='emergencyservicebooking',
            name='booking_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
