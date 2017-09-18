from django.db import models

# Create your models here.
class Distributor(models.Model):
    mobile = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField(default="")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = JSONField()