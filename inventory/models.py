from django.db import models

class Inventory(models.Model):
    DealerID = models.CharField(max_length=30)
    Brand = models.CharField(max_length=200)
    Model = models.CharField(max_length=500)
    PartIdentifier = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    MinQty = models.CharField(max_length=10)
    AvailableQty = models.CharField(max_length=20)
    NDP = models.CharField(max_length=30)
    MRP = models.CharField(max_length=30)
    IsCritical = models.CharField(max_length=10)
    AlternatePart = models.CharField(max_length=100)
