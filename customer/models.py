from django.db import models
from django.contrib.auth.models import User

class Vehicles(models.Model):
    VehicleType = models.CharField(max_length=20)
    Brand = models.CharField(max_length=200)
    Model = models.CharField(max_length=500)
    FuelType = models.CharField(max_length=20)
    RegNumber = models.CharField(max_length=200)
    YearOfManufacture = models.IntegerField()
    ChassisNumber = models.CharField(max_length=200)
    User = models.CharField(max_length=200)


class OTPTransactionInfo(models.Model):
    User = models.CharField(max_length=200)
    TranID = models.CharField(max_length=50)
    OTPValue = models.CharField(max_length=20)
    DateTime = models.CharField(max_length=50)
    VerificationStatus = models.CharField(max_length=20)


class Customer(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField(default="")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300, blank=True, default="")