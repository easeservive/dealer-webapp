import json
import datetime
import random
from django.utils import timezone

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError

import util
import log_rotator

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as status_code
from rest_framework.authtoken.models import Token
from rest_framework_jwt.settings import api_settings

from . import models
from . import forms


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


#############################


@api_view(['POST'])
def register(request):

    register_form = forms.RegisterForm(request.data)
    if not register_form.is_valid():
        return Response({'status': "failure", 'errors': register_form.errors}, status=status_code.HTTP_400_BAD_REQUEST)

    try:
        user_obj = User.objects.create_user(
            username = register_form.cleaned_data['mobile'],
            email = register_form.cleaned_data['email'],
            password = register_form.cleaned_data['password'],
            last_login = timezone.now()
        )

        customer_obj = models.Customer(
            mobile = register_form.cleaned_data['mobile'],
            first_name = register_form.cleaned_data['first_name'],
            last_name = register_form.cleaned_data['last_name'],
            address = register_form.cleaned_data['address']
        ).save()

    except IntegrityError:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        return Response({'status': "failure", 'msg': "User account already exists."}, status=status_code.HTTP_409_CONFLICT)
    
    status, otptranid = util.generateOTP(register_form.cleaned_data['mobile'])
    if status != 1:
        return Response({'status': "failure", 'msg': "OPT Failure"}, status=status_code.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'status': "success", 'msg': "Account creation successful.", 'otptranid': otptranid})


@api_view(['POST'])
def login(request):

    login_form = forms.LoginForm(request.data)
    if not login_form.is_valid():
        return Response({'status': "failure", 'errors': login_form.errors}, status=status_code.HTTP_400_BAD_REQUEST)

    # check if user account is activated
    user_obj = User.objects.get(username=login_form.cleaned_data['mobile'])
    if user_obj.is_active != 1:
        return Response({'status': "failure", 'msg': "User not verified."}, status=status_code.HTTP_401_UNAUTHORIZED)

    user = authenticate(username=login_form.cleaned_data['mobile'], password=login_form.cleaned_data['password'])
    if user is not None:
        user.last_login = timezone.now()
        user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        auth_token = jwt_encode_handler(jwt_payload_handler(user))
        # auth_token = Token.objects.get_or_create(user=user)
        # auth_token = auth_token[0].key

        return Response({'status': "success", 'msg': "Login successful.", 'auth_token': auth_token})
    else:
        return Response({'status': "failure", 'msg': "Invalid username/password."}, status=status_code.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def verify_otp(request):

    otp_form = forms.OtpForm(request.data)
    if not otp_form.is_valid():
        return Response({'status': "failure", 'errors': otp_form.errors}, status=status_code.HTTP_400_BAD_REQUEST)

    if not util.isValidOPT(otp_form.cleaned_data['otptranid'], otp_form.cleaned_data['otp_value']):
        return Response({"status": "failure", "msg": "Invalid OTP"}, status=status_code.HTTP_401_UNAUTHORIZED)

    return Response({"status": "success", "msg": "OTP successfully verified."})


@api_view(['POST'])
def resend_otp(request):

    otp_form = forms.ResendOtpForm(request.data)
    if not otp_form.is_valid():
        return Response({'status': "failure", 'errors': otp_form.errors}, status=status_code.HTTP_400_BAD_REQUEST)

    status, otptranid = util.generateOTP(otp_form.cleaned_data['mobile'])
    if status != 1:
        return Response({'status': "failure", 'msg': "OPT Failure"}, status=status_code.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'status': "success", 'otptranid': otptranid, 'msg': "OTP has been re-sent."})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def test(request):

    print("Auth success")

    return Response({'status': "success"})