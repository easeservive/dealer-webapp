from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_mysql.models import JSONField
#import urllib
import requests

class JCVehicleInfo(models.Model):
    VehicleNumber = models.CharField(max_length=20)
    Brand = models.CharField(max_length=200)
    Model = models.CharField(max_length=500)
    FuelType = models.CharField(max_length=20)
    ChassisNumber = models.CharField(max_length=200)
    CustomerName = models.CharField(max_length=50)
    ContactNumber = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
    KilometersTicked = models.CharField(max_length=20)
    CreatedTime = models.CharField(max_length=30)
    JobCardID = models.CharField(max_length=30)
    DealerID = models.CharField(max_length=30)


class JCStatus(models.Model):
    JobCardID = models.CharField(max_length=30)
    DealerID = models.CharField(max_length=30)
    MechanicName = models.CharField(max_length=30)
    DeliveryTime = models.CharField(max_length=30)
    service_reminder_time = models.CharField(max_length=30)
    Status = models.CharField(max_length=10)
    PendingReason = models.CharField(max_length=100)
    CreatedTime = models.CharField(max_length=30)
    LastedEditedTime = models.CharField(max_length=30)
    CustomerComplaint = models.TextField()
    ServiceTypeId = models.CharField(max_length=30)
    VehicleImages = JSONField()


class JCServiceDetails(models.Model):
    id = models.AutoField(primary_key=True)
    ServiceItem = models.CharField(max_length=1000)
    IsAvailed = models.CharField(max_length=10)
    JobCardID = models.CharField(max_length=30)
    DealerID = models.CharField(max_length=30)


class JCRecommendedServices(models.Model):
    id = models.AutoField(primary_key=True)
    JobCardID = models.CharField(max_length=30)
    DealerID = models.CharField(max_length=30)
    ServiceItems = models.TextField()


class JCStocksInfo(models.Model):
    id = models.AutoField(primary_key=True)
    PartIdentifier = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    UnitPrice = models.CharField(max_length=30)
    Qty = models.CharField(max_length=30)
    TotalPrice = models.CharField(max_length=30)
    JobCardID = models.CharField(max_length=30)
    DealerID = models.CharField(max_length=30)


class JCInvoiceAndLabourCost(models.Model):
    JobCardID = models.CharField(max_length=30)
    DealerID = models.CharField(max_length=30)
    MechanicName = models.CharField(max_length=30)
    InvoiceNumber = models.CharField(max_length=30)
    LabourCharge = models.CharField(max_length=30)
    PaymentMode = models.CharField(max_length=30)
    GeneratedTime = models.CharField(max_length=30)
    PartsTotalPrice = models.CharField(max_length=30)
    VATPercentage = models.CharField(max_length=30)
    TaxPercentage = models.CharField(max_length=30)
    

class JCOtherStocksInfo(models.Model):
    JobCardID = models.CharField(max_length=30)
    OtherPartsDesc = models.CharField(max_length=100)
    OtherPartsCost = models.CharField(max_length=30)


# Method for sendsms to customer 
@receiver(post_save)
def trigger_sms(sender, instance=None,created=False, **kwargs):

    '''Sending the SMS to customer 
    @@Prerequisites Bulk SMS API Credentials 
    @@ Creating the JobCard
    @@ Updating the JobCard
    @@ Closing the JobCard
    '''

    message = ""
    list_of_models = ('JCStatus')
    if sender.__name__ in list_of_models:
        jc_objs = JCVehicleInfo.objects.filter(JobCardID__iexact = instance.JobCardID)
        PhoneNo = str(jc_objs.get().ContactNumber)
        CustName = str(jc_objs.get().CustomerName)             
        if created:
            message = "Dear %s your vehicle service request is confirmed.JobCard ID:%s Status: %s DeliveryTime:%s"  %(CustName,instance.JobCardID,instance.Status,instance.DeliveryTime)
        else:
            if str(instance.Status) == "PENDING":
                message = "Dear %s your vehicle service in pending status.JobCard ID:%s Status: %s PendingReason:%s DeliveryTime:%s" %(CustName,instance.JobCardID,instance.Status,instance.PendingReason,instance.DeliveryTime) 
            elif str(instance.Status) == "CLOSED":
                message = "Dear %s your vehicle service is completed. JobCard ID:%s Status: %s  DeliveryTime:%s. Kindly visit the service center on time and collect your vehicle." %(CustName,instance.JobCardID,instance.Status,instance.DeliveryTime)
        #print(message)
        url=str("http://login.bulksmsgateway.in/sendmessage.php?user=easeservice&password=easeservice123!&message="+message+"&sender=EASESE&mobile="+PhoneNo+"&type=3")            
        #f = urllib.urlopen(url)
        #f.close()
        message_response = requests.get(url)
        print(message_response.json())


class CServiceBooking(models.Model):
    booking_id = models.CharField(primary_key=True, max_length=20)
    customer_id = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)
    vehicle_model_id = models.CharField(max_length=50)
    vehicle_registration_number = models.CharField(max_length=20)
    service_center_id = models.CharField(max_length=20)
    customer_address_id = models.CharField(max_length=20)
    service_details = models.TextField()
    feedback_stars = models.IntegerField(null=True, blank=True)
    feedback_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20)
    job_card_id = models.CharField(max_length=30, default=None, blank=True, null=True)


class EmergencyServiceBooking(models.Model):
    booking_id = models.CharField(primary_key=True, max_length=20)
    customer_id = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)
    customer_address_id = models.CharField(max_length=20)
    customer_latlon = models.CharField(max_length=100)
    service_details = models.TextField()
    feedback_stars = models.IntegerField(null=True, blank=True)
    feedback_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20)
    service_center_id = models.CharField(max_length=20)
    job_card_id = models.CharField(max_length=30, default=None, blank=True, null=True)