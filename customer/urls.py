from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from customer import views
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
   url('^api/create/user$', views.create_user),
   url('^api/login$', views.login_auth),
   url('^api/otp/verify$', views.verifyOTP),
   url('^api/otp/trigger$', views.triggerOTP),
   url('^api/forgotpw$', views.change_password),

   # REST
   url(r'^register$', views.register, name="register"),
   url(r'^login$', views.login, name="login"),
   url(r'^otp/verify$', views.verify_otp, name="verify_otp"),
   url(r'^otp/resend$', views.resend_otp, name="resend_otp"),
   url(r'^details$', views.retrieve_customer, name="retrieve_customer"),
   url(r'^address/add$', views.add_address, name="add_address"),
   url(r'^vehicle/add$', views.add_vehicle, name="add_vehicle"),
   url(r'^vehicle/tips$', views.retrieve_maintenance_tips, name="retrieve_maintenance_tips"),
   url(r'^remove$', views.remove_user, name="remove_user"),
   url(r'^test$', views.test, name="test"),


   # JWT
   url(r'^token-refresh$', refresh_jwt_token),
]

urlpatterns += staticfiles_urlpatterns()