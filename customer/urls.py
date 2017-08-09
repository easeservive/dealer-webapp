from django.conf.urls import url
from django.views.generic.base import TemplateView


from customer import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
               url('^api/create/user$', views.create_user),
               url('^api/login$', views.login_auth),
               url('^api/otp/verify$', views.verifyOTP),
               url('^api/otp/trigger$', views.triggerOTP),
               url('^api/forgotpw$', views.change_password),

]

urlpatterns += staticfiles_urlpatterns()
