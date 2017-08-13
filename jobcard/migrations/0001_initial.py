# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CServiceBooking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.CharField(max_length=20)),
                ('vehicle_type', models.CharField(max_length=50)),
                ('vehicle_model_id', models.CharField(max_length=20)),
                ('vehicle_registration_number', models.CharField(max_length=20)),
                ('service_center_id', models.CharField(max_length=20)),
                ('customer_address_id', models.CharField(max_length=20)),
                ('service_details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JCInvoiceAndLabourCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobCardID', models.CharField(max_length=30)),
                ('DealerID', models.CharField(max_length=30)),
                ('InvoiceNumber', models.CharField(max_length=30)),
                ('LabourCharge', models.CharField(max_length=30)),
                ('PaymentMode', models.CharField(max_length=30)),
                ('GeneratedTime', models.CharField(max_length=30)),
                ('PartsTotalPrice', models.CharField(max_length=30)),
                ('VATPercentage', models.CharField(max_length=30)),
                ('TaxPercentage', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='JCOtherStocksInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobCardID', models.CharField(max_length=30)),
                ('OtherPartsDesc', models.CharField(max_length=100)),
                ('OtherPartsCost', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='JCRecommendedServices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('JobCardID', models.CharField(max_length=30)),
                ('DealerID', models.CharField(max_length=30)),
                ('ServiceItems', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JCServiceDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ServiceItem', models.CharField(max_length=1000)),
                ('IsAvailed', models.CharField(max_length=10)),
                ('JobCardID', models.CharField(max_length=30)),
                ('DealerID', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='JCStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobCardID', models.CharField(max_length=30)),
                ('DealerID', models.CharField(max_length=30)),
                ('DeliveryTime', models.CharField(max_length=30)),
                ('service_reminder_time', models.CharField(max_length=30)),
                ('Status', models.CharField(max_length=10)),
                ('PendingReason', models.CharField(max_length=100)),
                ('CreatedTime', models.CharField(max_length=30)),
                ('LastedEditedTime', models.CharField(max_length=30)),
                ('ServiceType', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='JCStocksInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('PartIdentifier', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('UnitPrice', models.CharField(max_length=30)),
                ('Qty', models.CharField(max_length=30)),
                ('TotalPrice', models.CharField(max_length=30)),
                ('JobCardID', models.CharField(max_length=30)),
                ('DealerID', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='JCVehicleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleNumber', models.CharField(max_length=20)),
                ('Brand', models.CharField(max_length=200)),
                ('Model', models.CharField(max_length=500)),
                ('FuelType', models.CharField(max_length=20)),
                ('ChassisNumber', models.CharField(max_length=200)),
                ('CustomerName', models.CharField(max_length=50)),
                ('ContactNumber', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=200)),
                ('KilometersTicked', models.CharField(max_length=20)),
                ('CreatedTime', models.CharField(max_length=30)),
                ('JobCardID', models.CharField(max_length=30)),
                ('DealerID', models.CharField(max_length=30)),
            ],
        ),
    ]
