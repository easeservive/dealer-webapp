from django.conf.urls import url
from django.views.generic.base import TemplateView


#from django.conf.urls import url
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
     url('^$', views.home),
     url('^test/$', views.test),
     url('^mesh/$', views.meshup),
     url('^success/$', views.success),
     #url('^dealer/home$', views.dealerhome),
     #url('^contact$', views.contact),
     url('^api/categories$', views.categories),
     #url('^api/create/user$', views.create_user),
     #url('^api/login$', views.login),
     #url('^api/otp/verify$', views.verifyOTP),
     #url('^api/otp/trigger$', views.triggerOTP),
     #url('^api/forgotpw$', views.change_password),
     #url('^api/add/vehicle$', views.addvehicle),
     #url('^api/get/sch_maintenance$', views.fetch_scheduled_maintenance),
     #url('^api/estimate/spares$', views.estimate_parts),
     #url('^api/create/jobcard$', views.create_job_card),
     url('^api/get/serviceitems$', views.fetch_service_items),
     #url('^api/save/jobcard$', views.save_job_card),
     #url('^api/auto/jobs$', views.data_for_jobs_auto_suggestion),
     #url('^api/auto/spares$', views.data_for_parts_auto_suggestion),
     url('^api/dashboard$', views.dashboard_data),
     url('^api/service/history$', views.service_history_data),

     # REST
     url(r'^apis/core/v1/servicecenter$', views.retrieve_service_center, name="retrieve_service_center"),
     url(r'^apis/core/v1/surveys$', views.retrieve_surveys, name="retrieve_surveys"),
     url(r'^apis/core/v1/reviews/vehicle$', views.retrieve_vehicle_review, name="retrieve_vehicle_review"),
     url(r'^apis/core/v1/vehicle/models$', views.retrieve_vehicle_models, name="retrieve_vehicle_models"),\
     url(r'^apis/core/v1/servicecenter/all$', views.retrieve_service_centers, name="retrieve_service_centers"),

]

urlpatterns += staticfiles_urlpatterns()
