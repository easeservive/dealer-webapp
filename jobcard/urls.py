from django.conf.urls import url
from django.views.generic.base import TemplateView

from jobcard import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
               url('^api/add/vehicle$', views.addvehicle),
               url('^api/get/sch_maintenance$', views.fetch_scheduled_maintenance),
               url('^api/estimate/spares$', views.estimate_parts),
               url('^api/create/jobcard/$', views.create_job_card),
               url('^api/get/jobcard$', views.fetch_job_card),
               url('^api/save/jobcard$', views.save_job_card),
               url('^api/generate/invoice/$', views.generate_invoice),
               url('^api/auto/jobs$', views.data_for_jobs_auto_suggestion),
               url('^api/auto/spares$', views.data_for_parts_auto_suggestion),
               url('^api/get/jobcards/$', views.get_jobcards_list),

]

urlpatterns += staticfiles_urlpatterns()
