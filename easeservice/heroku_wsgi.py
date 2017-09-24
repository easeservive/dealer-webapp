"""
WSGI config for easeservice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
if os.environ['ENV_TYPE'] == "00":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easeservice.local_settings")
elif os.environ['ENV_TYPE'] == "01":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easeservice.stage_settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)