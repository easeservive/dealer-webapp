# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('mobile', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(default='', max_length=254)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', django_mysql.models.JSONField(default=dict)),
                ('vehicles', django_mysql.models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='OTPTransactionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=200)),
                ('TranID', models.CharField(max_length=50)),
                ('OTPValue', models.CharField(max_length=20)),
                ('DateTime', models.CharField(max_length=50)),
                ('VerificationStatus', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleType', models.CharField(max_length=20)),
                ('Brand', models.CharField(max_length=200)),
                ('Model', models.CharField(max_length=500)),
                ('FuelType', models.CharField(max_length=20)),
                ('RegNumber', models.CharField(max_length=200)),
                ('YearOfManufacture', models.IntegerField()),
                ('ChassisNumber', models.CharField(max_length=200)),
                ('User', models.CharField(max_length=200)),
            ],
        ),
    ]
