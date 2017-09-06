import traceback

from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.files.images import ImageFile
from django.db import IntegrityError

from .models import ServiceCenterInfo

import json
import datetime
import random

import util
import log_rotator

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as status_code

from . import models
from . import forms

# Create your views here.

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

def test(request):
    result = {"status": "success", "msg": "It works"}
    lis1 = '<input type="checkbox" name="serv1" value="Change Oil" checked="checked"> Change Oil<br>'
    lis2 = '<input type="checkbox" name="serv2" value="Check filter" checked="checked"> Check filter<br>'
    lis3 = '<input type="checkbox" name="serv3" value="Check tyre pressure" checked="checked"> Check tyre pressure<br>'
    result['scheduled'] = lis1 + lis2 + lis3
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

def meshup(request):
    try:
        if request.method == 'POST':
            service_center_name = request.POST.get('service_center_name', 'NA')
            building_no = request.POST.get('building_no', 'NA')
            street_name = request.POST.get('street_name', 'NA')
            town = request.POST.get('town', 'NA')
            district = request.POST.get('district', 'NA')
            city = request.POST.get('city', 'NA')
            pin_code = request.POST.get('pin_code', 'NA')
            email = request.POST.get('email', 'NA')
            contact_no = request.POST.get('contact_no', 'NA')
            owner_name = request.POST.get('owner_name', 'NA')
            specialization = request.POST.get('specialization', 'NA')
            #images = request.POST.get('img', 'NA')
            #image_ids = []
            #error_logger = log_rotator.error_logger()
            #error_logger.debug(str(request))
            #error_logger.debug(dir(request.FILES))
            #if isinstance(images, list):
            #    for image in request.FILES.getlist("file[]"):
            #        error_logger.debug(str(image))
            #        image_id = "IMG" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '_' + str(random.randint(111, 999)) + '.jpg'
            #        handle_uploaded_file(ImageFile(image), image_id)
            #        image_ids.append(image_id)
            #    ServiceCenterInfo.objects.create(Name = service_center_name,
            #                                 ContactNumber = contact_no,
            #                                 Email = email,
            #                                 BuildingNo = building_no,
            #                                 Street = street_name,
            #                                 Town  = town,
            #                                 District = district,
            #                                 City = city,
            #                                 Pincode = pin_code,
            #                                 OwnerName = owner_name,
            #                                 Specialization = specialization,
            #                                 Images = ",".join(image_ids))
            #else:
            #    image_id = "IMG" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '_' +str(random.randint(111, 999)) + '.jpg'
            #    #if util.save_image(image_id, images):
            #    #    image_ids.append(image_id)
            #    handle_uploaded_file(ImageFile(request.FILES['img']), image_id)
            ServiceCenterInfo.objects.create(
                Name = service_center_name,
                ContactNumber = contact_no,
                Email = email,
                BuildingNo = building_no,
                Street = street_name,
                Town  = town,
                District = district,
                City = city,
                Pincode = pin_code,
                OwnerName = owner_name,
                Specialization = specialization
            )
            
            t = get_template('home.html')
            html = t.render({'show_success': True, 'show_failure': False})
            return HttpResponse(html) 
            #redirect('/?post=success')
        else:
            result = {'status': 'error', 'msg': 'Invalid Request method.'}
            return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        t = get_template('home.html')
        html = t.render({'show_success': False, 'show_failure': True})
        return HttpResponse(html)


def handle_uploaded_file(f, name):
    path_to_file = '/var/www/html/images/%s'%name 
    #with open(path_to_file, 'wb+') as destination:
    #    for chunk in f.chunks():
    #        destination.write(chunk)
    import shutil
    with open(path_to_file, 'wb') as fout:
        shutil.copyfileobj(f, fout, 100000)

def success(request):
    image = util.get_image()
    t = get_template('success.html')
    html = t.render({'image': image})
    return HttpResponse(html)

def home(request):
    """
    @summary: View method to check the server status.
    @param request: HttpRequest.
    @rtype: HttpResponse
    @return: HttpResponse containing server status.
    """
    show_success = False
    show_failure = False
    if request.GET.get('post') == 'success':
        show_success = True
    elif request.GET.get('post') == 'failure':
        show_failure = True
    t = get_template('home.html')
    #html = t.render(Context({'show_success': show_success, 'show_failure': show_failure}))
    html = t.render({'show_success': show_success, 'show_failure': show_failure})
    return HttpResponse(html)

def dealerhome(request):
    """
    @summary: View method to check the server status.
    @param request: HttpRequest.
    @rtype: HttpResponse
    @return: HttpResponse containing server status.
    """
    t = get_template('dealerhome.html')
    html = t.render({})
    return HttpResponse(html)

def categories(request):
    result = {"bikes": {}, "cars": {}}
    bike_data = Bikes.objects.all()
    for obj in bike_data:
        result["bikes"][obj.Brand] = eval(obj.Models)
    car_data = Cars.objects.all()
    for obj in car_data:
        result["cars"][obj.Brand] = eval(obj.Models)
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

#def create_user(request):
#
#    try:
#      if request.method == 'POST':
#        data = request.POST
#        user = data['mobile']
#        emailid = data['emailid']
#        passwd = data['passwd']
#        fname = data['fname']
#        lname = data['lname']
#
#        user_obj = User.objects.create_user(username = user,
#                                   email = emailid,
#                                   password = passwd)
#        user_obj.first_name = fname
#        user_obj.last_name = lname
#        user_obj.is_active = 0
#
#        user_obj.save()
#        
#        status, otptranid = util.generateOTP(user)
#        if status == 1:
#            result = {"status": "success", "msg": "successfully created an user account", "otptranid": otptranid}
#        else:
#            result = {"status": "success", "msg": "successfully created an user account but error in triggering otp", "otptranid": otptranid}
#      else:
#        result = {"status": "failure", "msg": "Invalid request method"}
#    except KeyError:
#        result = {"status": "failure", "msg": "Mandatory data missing"}
#    except IntegrityError:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "User account already exists."}
#    except:
#      print traceback.format_exc()
#      result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
#def verifyOTP(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#            tranid = data.get('tran_id', 'NA')
#            otpvalue = data.get('otp_value', 'NA')
#            if util.isValidOPT(tranid, otpvalue):
#                result = {"status": "success", "msg": "OTP successfully verified"}
#            else:
#                result = {"status": "failure", "msg" : "Invalid OTP"}
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
#def triggerOTP(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#            user = data.get('mobile', 'NA')
#            status, otptranid = util.generateOTP(user)
#            if status == 1:
#                result = {"status": "success", "otptranid": otptranid}
#            else:
#                result = {"status": "failure", "otptranid": otptranid}
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
#def login(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#            username = data.get('user', 'NA')
#            passwd = data.get('passwd', 'NA')
#
#            user = authenticate(username=username, password=passwd)
#            if user is not None:
#                # the password verified for the user
#                if user.is_active:
#                    request.session.__setitem__('user', username)
#                    result = {"status" : "success", "msg": "User is valid, active and authenticated"}
#                else:
#                    result = {"status" : "failure", "msg": "The password is valid, but the account has been disabled!"}
#            else:
#                # the authentication system was unable to verify the username and password
#                result = {"status" : "failure", "msg": "The username and password were incorrect."}
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
#
#def change_password(request):
#    try:
#      if request.method == 'POST':
#          data = request.POST
#          username = data.get('user', 'NA')
#          passwd = data.get('passwd', 'NA')
#          tranid = data.get('tran_id', 'NA')
#          result = resetPassword(username, passwd, tranid)
#          #u = User.objects.get(username=username)
#          #u.set_password(passwd)
#          #u.save()
#          #result = {"status" : "success", "msg": "Password has been updated successfully."}
#      else:
#          result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#      print traceback.format_exc()
#      result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

#def addvehicle(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#            type = data.get('type', 'NA')
#            brand = data.get('brand', 'NA')
#            model = data.get('model', 'NA')
#            fuel_type = data.get('fuel_type', 'NA')
#            chasis_number = data.get('c_num', 'NA')
#            year_of_man = data.get('man_year', 'NA')
#            reg_num = data.get('reg_num', 'NA')
#            user = request.session.get('user', 'NA')
#            vehicle = Vehicles.objects.create(VehicleType = type,
#                                              Brand  = brand,
#                                              Model = model,
#                                              FuelType = fuel_type,
#                                              RegNumber = reg_num,
#                                              YearOfManufacture = year_of_man,
#                                              ChasisNumber = chasis_number,
#                                              User = user)
#            result = {"status" : "success", "msg": "Added successfully"}
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
#def fetch_scheduled_maintenance(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#            brand = data.get('brand', 'NA')
#            model = data.get('model', 'NA')
#            fuel_type = data.get('fuel_type', 'NA')
#            km_ticked = int(data.get('km_ticked', '0'))
#            print brand, model, fuel_type, km_ticked
#            print type(brand), type(model), type(fuel_type), type(km_ticked)
#            result = util.fetchScheduledServices(brand, model, fuel_type, km_ticked)
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
def fetch_service_items(request):
    try:
        if request.method == 'POST':
            data = request.POST
            result = {"status" : "success", "services": ["Water wash", "Air Filter Change", "Wheel Align"]}
            #result = util.fetchScheduledServices(brand, model, fuel_type, km_ticked)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        print(traceback.format_exc())
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

#def estimate_parts(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#            parts = data.get('parts', 'NA')
#            dealerid = data.get('dealerid', 'NA')
#            result = util.getEstimate(parts, dealerid)
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
#def fetch_job_card(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#            print data
#            jc_id = data.get('jc_id', 'NA')
#            dealerid = data.get('dealerid', 'NA')
#            result = util.getJobCard(jc_id, dealerid)
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
#def create_job_card(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#            dealerid = data.get('dealerid', 'NA')
#            details = {}
#  
#            details['veh_num'] = data['veh_num']
#            details['brand'] = data['brand']
#            details['model'] = data['model']
#            details['fuel_type'] = data['fuel_type']
#            details['c_num'] = data['c_num']
#            details['cust_name'] = data['cust_name']
#            details['cont_num'] = data['cont_num']
#            details['cont_address'] = data['cont_address']
#            details['km_ticked'] = data['km_ticked']
#
#            details['del_time'] = data['del_time'] 
#            details['status'] = data['status']
#            details['reason'] = data['reason']
#
#            details['services'] = data['services']
#            details['spares'] = data['spares']
#            result = util.createJobCard(details, dealerid)
#
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
#def save_job_card(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#            dealerid = data.get('dealerid', 'NA')
#            jc_id = data.get('jc_id', 'NA')
#            details = {}
#            
#            details['jc_id'] = data.get('jc_id', 'NA')
#            details['veh_num'] = data['veh_num']
#            details['brand'] = data['brand']
#            details['model'] = data['model']
#            details['fuel_type'] = data['fuel_type']
#            details['c_num'] = data['c_num']
#            details['cust_name'] = data['cust_name']
#            details['cont_num'] = data['cont_num']
#            details['cont_address'] = data['cont_address']
#            details['km_ticked'] = data['km_ticked']
#
#            details['del_time'] = data['del_time']
#            details['status'] = data['status']
#            details['reason'] = data['reason']
#
#            details['services'] = data['services']
#            details['spares'] = data['spares']
#
#            result = util.saveJobCard(details, dealerid, jc_id)
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
#def data_for_jobs_auto_suggestion(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
#def data_for_parts_auto_suggestion(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
#
#def generate_invoice(request):
#    try:
#        if request.method == 'POST':
#            data = request.POST
#            jc_id = data['jc_id']
#            result = util.generateInvoice(jc_id)
#        else:
#            result = {"status": "failure", "msg": "Invalid request method"}
#    except:
#        print traceback.format_exc()
#        result = {"status": "failure", "msg": "something went wrong"}
#    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

def dashboard_data(request):
    try:
        if request.method == 'POST':
            data = request.POST
            dealerid = data.get('dealerid', 'NA')
            result = util.getDashboardData(dealerid)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        print(traceback.format_exc())
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

def service_history_data(request):
    try:
        error_logger = log_rotator.error_logger()
        if request.method == 'POST':
            if request.user.is_authenticated():
                error_logger.debug(request)
                data = request.POST
                veh_num = data.get('veh_num', '')
                c_num = data.get('c_num', '')
                if veh_num or c_num:
                    result = util.fetchServiceHistory(veh_num, c_num)
                else:
                    result = {"status": "failure", "msg": "Mandatory post data missing."}
            else:
                result = {"status": "unauthorized", "msg": "Not authorized", "url": "/dealer/login/"}
        else: 
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        print(traceback.format_exc())
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def retrieve_service_center(request):

    service_form = forms.RetrieveServiceCenter(request.GET)
    if not service_form.is_valid():
        return Response({'status': "failure", 'errors': service_form.errors}, status=status_code.HTTP_400_BAD_REQUEST)

    try:
        service_center_obj = models.ServiceCenterInfo.objects.get(id=service_form.cleaned_data['service_center_id'])
    except models.ServiceCenterInfo.DoesNotExist:
        return Response({'status': "failure", "msg": "Invalid service_center_id."}, status=status_code.HTTP_409_CONFLICT)

    return Response({
        'status': "success",
        "service_center_data": {
            "name": service_center_obj.Name,
            "contact_number": service_center_obj.ContactNumber,
            "email": service_center_obj.Email,
            "building_number": service_center_obj.BuildingNo,
            "street": service_center_obj.Street,
            "town": service_center_obj.Town,
            "district": service_center_obj.District,
            "city": service_center_obj.City,
            "pincode": service_center_obj.Pincode,
            "owner_name": service_center_obj.OwnerName,
            "specilization": service_center_obj.Specialization,
            "images": service_center_obj.Images
        }
    })


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def retrieve_surveys(request):

    surveys_objects = models.Surveys.objects.filter(survey_availability=1)

    surveys_list = []
    for survey_obj in surveys_objects:
        surveys_list.append({
            "survey_id": survey_obj.id,
            "title": survey_obj.title,
            "description": survey_obj.description,
            "survey_url": survey_obj.survey_url,
            "created_at": survey_obj.created_at,
            "ends_at": survey_obj.ends_at,
        })

    return Response({'status': "success", "surveys_list": surveys_list})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def retrieve_vehicle_review(request):

    review_form = forms.RetrieveVehicleReview(request.GET)
    if not review_form.is_valid():
        return Response({'status': "failure", 'errors': review_form.errors}, status=status_code.HTTP_400_BAD_REQUEST)

    try:
        vehicle_obj = models.VehicleModels.objects.get(vehicle_model_id=review_form.cleaned_data['vehicle_model_id'])
    except models.VehicleModels.DoesNotExist:
        return Response({'status': "failure", "msg": "Invalid Vehicle Model."}, status=status_code.HTTP_400_BAD_REQUEST)

    try:
        vehicle_review_obj = models.VehicleReviews.objects.get(vehicle_model_id=review_form.cleaned_data['vehicle_model_id'])
    except models.VehicleReviews.DoesNotExist:
        vehicle_review_obj = None

    vehicle_data = {
        'vehicle_name': vehicle_obj.vehicle_name,
        'model_name': vehicle_obj.model_name,
        'brand_name': vehicle_obj.brand_name
    }

    if vehicle_review_obj:
        vehicle_data['stars'] = vehicle_review_obj.stars
        vehicle_data['text'] = vehicle_review_obj.text
        vehicle_data['user_count'] = vehicle_review_obj.user_count
    else:
        # stars = 0 depicts that there is no review for this model, catch 0 and display no reviews in frontend
        vehicle_data['stars'] = 0
        vehicle_data['text'] = "Not Available"
        vehicle_data['user_count'] = "Not Available"

    return Response({'status': "success", "vehicle_data": vehicle_data})