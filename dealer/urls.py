from django.conf.urls import url
from django.views.generic.base import TemplateView


#from django.conf.urls import url
from dealer import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
               url('^dealer/login/$', views.login_dealer),
               url('^dealer/home/$', views.home),
               url('^dealer/logout/$', views.logout_dealer),
               url('^dealer/service/history/$', views.get_service_history),
               url('^dealer/inventory/$', views.get_inventory),
               #url('^dealer/update/inventory/(?P<identifier>.*)/$', views.get_inventory),
               url('^dealer/update/inventory/*$', views.update_inventory),
               url('^jobcard/$', views.jobcard_home),
               url('^jobcard/new/$', views.jobcard_new),
               url('^jobcard/edit/$', views.jobcard_edit),
               url('^invoice/$', views.generate_invoice),
               url('^view/invoice/$', views.view_invoice),

]

urlpatterns += staticfiles_urlpatterns()
