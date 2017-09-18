import binascii
import os
from itsdangerous import URLSafeTimedSerializer
from django.conf import settings

def generate_uuid(count):
    return binascii.hexlify(os.urandom(count)).decode()


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    return serializer.dumps(email, salt=settings.SECURITY_PASSWORD_SALT)