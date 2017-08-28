from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import JSONField

class Vehicles(models.Model):
    vehicle_model_id = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    vehicle_registration_number = models.CharField(max_length=30, primary_key=True)
    year = models.IntegerField()
    chassis_number = models.CharField(max_length=200)
    customer_id = models.CharField(max_length=20)
    total_kms = models.IntegerField()


class OTPTransactionInfo(models.Model):
    User = models.CharField(max_length=200)
    TranID = models.CharField(max_length=50)
    OTPValue = models.CharField(max_length=20)
    DateTime = models.CharField(max_length=50)
    VerificationStatus = models.CharField(max_length=20)


class Customer(models.Model):
    mobile = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField(default="")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = JSONField()
    vehicles = JSONField()