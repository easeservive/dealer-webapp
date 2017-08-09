from django.conf.urls import url
from django.views.generic.base import TemplateView

from inventory import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
               url('^api/get/inventory$', views.auto_suggest_inventory),
               url('^api/update/inventory$', views.updateStocks),

]

urlpatterns += staticfiles_urlpatterns()
