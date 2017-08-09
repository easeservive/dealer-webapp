from django.db import models


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
