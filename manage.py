#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":

    if ( 
      	'ENV_TYPE' in os.environ and 
      	os.environ['ENV_TYPE'] == "00" 
      	): 
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easeservice.local_settings") 
    else: 
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easeservice.settings") 

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
