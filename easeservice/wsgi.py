"""
WSGI config for easeservice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

server_config = os.getenv("SERVER_ENV")

os.environ['PYTHON_EGG_CACHE'] = '/tmp/egg'

if server_config and server_config.__contains__("Development"):
    sys.path.append("/host/Ease/easeserver/easeservice")
else:
	sys.path.append("/var/ease/dealer-webapp")
    #sys.path.append("/var/www/html/easeserver/easeservice")
sys.path.append("/host/Ease/easeserver/easeservice")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easeservice.settings")
application = get_wsgi_application()
