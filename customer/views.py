import json
import datetime
import random

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError

import util
import log_rotator


def json_default(obj):
    """
    @summary: Method to convert decimal and datetime in response to string.
    @param obj: decimal/datetime object
    @rtype: string
    @return: string object
    """
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    if isinstance(obj, datetime.date):
        return str(obj)
    raise TypeError


def create_user(request):

    try:
        if request.method == 'POST':
            data = request.POST
            user = data['mobile']
            emailid = data['emailid']
            passwd = data['passwd']
            fname = data['fname']
            lname = data['lname']

            user_obj = User.objects.create_user(username = user,
                                   email = emailid,
                                   password = passwd)
            user_obj.first_name = fname
            user_obj.last_name = lname
            user_obj.is_active = 0

            user_obj.save()

            status, otptranid = util.generateOTP(user)
            if status == 1:
                result = {"status": "success",
                "msg": "successfully created an user account",
                "otptranid": otptranid}
            else:
                result = {"status": "success",
                "msg": "successfully created an user account but error in triggering otp",
                "otptranid": otptranid}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except KeyError:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Mandatory data missing"}
    except IntegrityError:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "User account already exists."}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def verifyOTP(request):
    try:
        if request.method == 'POST':
            data = request.POST
            tranid = data.get('tran_id', 'NA')
            otpvalue = data.get('otp_value', 'NA')
            if util.isValidOPT(tranid, otpvalue):
                result = {"status": "success", "msg": "OTP successfully verified"}
            else:
                result = {"status": "failure", "msg": "Invalid OTP"}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def triggerOTP(request):
    try:
        if request.method == 'POST':
            data = request.POST
            user = data.get('mobile', 'NA')
            status, otptranid = util.generateOTP(user)
            if status == 1:
                result = {"status": "success", "otptranid": otptranid}
            else:
                result = {"status": "failure", "otptranid": otptranid}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}

    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def login_auth(request):
    try:
        if request.method == 'POST':
            data = request.POST
            view_logger = log_rotator.view_logger()
            view_logger.debug("LOGIN DEATILS:: %s :"%(data))
            view_logger.debug("LOGIN DEATILS REQQQ:: %s :"%(request))
            username = data.get('user', 'NA')
            passwd = data.get('passwd', 'NA')

            view_logger = log_rotator.view_logger()
            user = authenticate(username=username, password=passwd)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    request.session.__setitem__('user', username)
                    result = {"status": "success", "msg": "User is valid, active and authenticated"}
                    view_logger.debug("DEALER VIEW : Service history request for %s"%request.user)
                else:
                    result = {"status": "failure", "msg": "The password is valid, but the account has been disabled!"}
            else:
                # the authentication system was unable to verify the username and password
                result = {"status": "failure", "msg": "The username and password were incorrect."}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def change_password(request):
    try:
        if request.method == 'POST':
            data = request.POST
            username = data.get('user', 'NA')
            passwd = data.get('passwd', 'NA')
            tranid = data.get('tran_id', 'NA')
            result = util.resetPassword(username, passwd, tranid)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
