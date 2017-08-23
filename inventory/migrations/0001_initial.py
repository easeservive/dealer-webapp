# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DealerID', models.CharField(max_length=30)),
                ('Brand', models.CharField(max_length=200)),
                ('Model', models.CharField(max_length=500)),
                ('PartIdentifier', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('MinQty', models.CharField(max_length=10)),
                ('AvailableQty', models.CharField(max_length=20)),
                ('NDP', models.CharField(max_length=30)),
                ('MRP', models.CharField(max_length=30)),
                ('IsCritical', models.CharField(max_length=10)),
                ('AlternatePart', models.CharField(max_length=100)),
            ],
        ),
    ]
