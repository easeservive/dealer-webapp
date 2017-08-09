from django.db import models


class ScheduledServices(models.Model):
    Brand = models.CharField(max_length=200)
    Model = models.CharField(max_length=500)
    FuelType = models.CharField(max_length=20)
    MinKM = models.IntegerField()
    MaxKM = models.IntegerField()
    ServiceIdentifier = models.CharField(max_length=100)


class ScheduledServiceDetails(models.Model):
    ServiceIdentifier = models.CharField(max_length=100)
    ServiceInfo = models.CharField(max_length=1000)
    Parts = models.CharField(max_length=500)

class ComplaintCode(models.Model):
    Code = models.CharField(max_length=10, primary_key = True)
    Description = models.CharField(max_length=70)
    Aggregate = models.CharField(max_length=50)


class ServiceCenterInfo(models.Model):
    Name = models.CharField(max_length=200)
    ContactNumber = models.CharField(max_length=50)
    Email = models.CharField(max_length=200)
    BuildingNo = models.CharField(max_length=50)
    Street = models.CharField(max_length=200)
    Town  = models.CharField(max_length=200)
    District = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Pincode = models.CharField(max_length=20)
    OwnerName = models.CharField(max_length=100)
    Specialization = models.CharField(max_length=1000)
    Images = models.CharField(max_length=1000)

class SupportedCarBrands(models.Model):
    Brand  = models.CharField(max_length=200)

#class SupportedVehicles(models.Model):
#    Brand  = models.CharField(max_length=200)
#    Models = models.CharField(max_length=5000)
#    Type = models.CharField(max_length=20)
#

