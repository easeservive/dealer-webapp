from django.conf.urls import url
from django.views.generic.base import TemplateView

from jobcard import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   #url('^api/add/vehicle$', views.addvehicle),
   url('^api/get/sch_maintenance$', views.fetch_scheduled_maintenance),
   url('^api/estimate/spares$', views.estimate_parts),
   url('^api/create/jobcard/$', views.create_job_card),
   url('^api/get/jobcard$', views.fetch_job_card),
   url('^api/save/jobcard$', views.save_job_card),
   url('^api/generate/invoice/$', views.generate_invoice),
   url('^api/auto/jobs$', views.data_for_jobs_auto_suggestion),
   url('^api/auto/spares$', views.data_for_parts_auto_suggestion),
   url('^api/get/jobcards/$', views.get_jobcards_list),

   # REST
   url(r'^apis/jobcard/v1/service/book$', views.book_service, name="book_service"),
   url(r'^apis/jobcard/v1/service/details$', views.retrieve_service_details, name="retrieve_service_details"),
   url(r'^apis/jobcard/v1/service/history$', views.retrieve_service_history, name="retrieve_service_history"),
   url(r'^apis/jobcard/v1/service/feedback/add$', views.add_service_feedback, name="add_service_feedback"),
   url(r'^apis/jobcard/v1/emergency/service/book$', views.book_emergency_service, name="book_emergency_service"),
   url(r'^apis/jobcard/v1/emergency/service/details$', views.retrieve_emergency_service, name="retrieve_emergency_service"),

   url(r'^apis/jobcard/v1/service/requests$', views.retrieve_service_requests, name="retrieve_service_requests"),
   url(r'^apis/jobcard/v1/service/accept$', views.accept_service_request, name="accept_service_request"),
]

urlpatterns += staticfiles_urlpatterns()
