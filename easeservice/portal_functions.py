import binascii
import os

def generate_uuid(count):
    return binascii.hexlify(os.urandom(count)).decode()