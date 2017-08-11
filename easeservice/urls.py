"""easeservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

#from django.conf.urls import patterns, include, url
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#import sys

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'', include('dealer.urls')),
    url(r'', include('inventory.urls')),
    url(r'', include('jobcard.urls')),
    url(r'^apis/customer/v1/', include('customer.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.autodiscover()


#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'mobile.views.home', name='home'),
#    # url(r'^mobile/', include('mobile.foo.urls')),
#
#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#    # Uncomment the next line to enable the admin:
#    # url(r'^admin/', include(admin.site.urls)),
#    url(r'', include('core.urls')),
#)

#urlpatterns += staticfiles_urlpatterns()

# urlpatterns += [
#     url(r'', include('core.urls')),
#     url(r'', include('customer.urls')),
#     url(r'', include('dealer.urls')),
#     url(r'', include('inventory.urls'))
#     url(r'', include('jobcard.urls')),
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = patterns(
#     '',
#     url(r'', include('core.urls')),
#     url(r'', include('customer.urls')),
#     url(r'', include('jobcard.urls')),
#     url(r'', include('dealer.urls')),
#     url(r'', include('inventory.urls')),
#     url(r'^admin/', admin.site.urls),
#     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
# ) 
