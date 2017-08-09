from django.contrib import admin
from .models import ServiceCenterInfo
# Register your models here
class ServiceCenterInfoAdmin(admin.ModelAdmin):
    list_display = ['Name','City','OwnerName']
    list_filter = ['OwnerName','City']


admin.site.register(ServiceCenterInfo, ServiceCenterInfoAdmin)