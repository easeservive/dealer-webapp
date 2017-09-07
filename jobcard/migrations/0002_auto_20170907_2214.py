# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cservicebooking',
            name='vehicle_type',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cservicebooking',
            name='job_card_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cservicebooking',
            name='vehicle_model_id',
            field=models.CharField(max_length=20),
        ),
    ]