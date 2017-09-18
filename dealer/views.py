from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template import Context
from easeservice import global_constants

import json
import decimal
import datetime

import log_rotator
import util

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

def login_dealer(request):
    """
    @summary: View method to check the server status.
    @param request: HttpRequest.
    @rtype: HttpResponse
    @return: HttpResponse containing server status.
    """
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'POST':
            data = request.POST
            username = data.get('user', 'NA')
            passwd = data.get('passwd', 'NA')
            view_logger.debug("Dealer login request for : %s"%username)
            user = authenticate(username=username, password=passwd)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    request.session.__setitem__('user', username)
                    result = {"status": "success", "url": "/dealer/home/"}
                else:
                    result = {"status": "failure", "msg": "The password is valid, but the account has been disabled!"}
            else:
                # the authentication system was unable to verify the username and password
                result = {"status": "failure", "msg": "The username and password were incorrect."}
            view_logger.debug("Dealer login response for %s : %s"%(username, str(result)))

            ######## TEST
            #service_center_id = request.sess
            request.session['service_center_id'] = "TEST123"
            ######## TEST

            return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
        elif request.method == 'GET':
            view_logger.debug("Dealer login GET request for : %s"%request.user)
            if request.user.is_authenticated():
                view_logger.debug("%s already logged in. Redirecting to home page."%request.user)
                return redirect('/dealer/home/')
            t = get_template('dealerlogin.html')
            html = t.render({})
            view_logger.debug("Rendered login page.")
            return HttpResponse(html)
        else:
            result = {'status': 'error', 'msg': 'Invalid Request method.'}
            return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {'status': 'error', 'msg': 'Something went wrong.'}
        return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def home(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'GET':
            if not request.user.is_authenticated():
               view_logger.debug("Home page request. Not logged in. Redirecting to home page.")
               return redirect('/dealer/login/')
            t = get_template('dashboard.html')
            user_agent = "all"
            user_agent=request.META.get("HTTP_USER_AGENT")
            view_logger.debug("USER AGENT : %s"%user_agent)
            if "Android" in user_agent:
                user_agent = "android"

            view_logger.debug("Home page request for : %s"%request.user)
            context_dictionary = util.getDashboardData(request.user)
            context_dictionary['user'] = request.user
            context_dictionary['user_agent'] = user_agent
            html = t.render(context_dictionary)
            view_logger.debug("Rendered home page for : %s"%request.user)
            return HttpResponse(html)
        else:
            result = {'status': 'error', 'msg': 'Invalid Request method.'}
            return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {'status': 'error', 'msg': 'Something went wrong.'}
        return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def logout_dealer(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'POST':
            view_logger.debug("Logout request for %s through POST method"%request.user)
            logout(request)
            result = {"status": "success", "msg": "User is valid, active and authenticated"}
            return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
        elif request.method == 'GET':
            view_logger.debug("Logout request for %s through GET method"%request.user)
            logout(request)
            return redirect('/dealer/login/')
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def get_service_history(request):
    try:
        view_logger = log_rotator.view_logger()
        view_logger.debug("SERVICE HISTORY details: %s :"%(request))
        if request.method == 'GET':
            view_logger.debug("DEALER VIEW : Service history request for %s"%request.user)
            if not request.user.is_authenticated():
                view_logger.debug("DEALER VIEW : Redirected %s to login from service history"%request.user)
                return redirect('/dealer/login/')
            t = get_template('servicehistory.html')
            #util.fetchServiceHistory(veh_num, c_num)
            #context_dictionary['user'] = request.user
            html = t.render({'user': request.user})
            view_logger.debug("DEALER VIEW : Rendered service history for : %s"%request.user)
            return HttpResponse(html)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
        return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def get_inventory(request):
    try:
        view_logger = log_rotator.view_logger()

        view_logger.debug("INVENTORY details: %s :"%(request))
        view_logger.debug("INVENTORY user: %s :"%(request.user))
        if request.method == 'GET':
            view_logger.debug("DEALER VIEW : Get inventory request for %s through GET method"%request.user)
            if not request.user.is_authenticated():
                view_logger.debug("DEALER VIEW : Redirected %s to login from get inventory"%request.user)
                return redirect('/dealer/login/')
            t = get_template('inventory.html')
            html = t.render({'user': request.user})
            view_logger.debug("DEALER VIEW : Rendered Get Inventory page for : %s"%request.user)
            return HttpResponse(html)
        elif request.method == 'POST':
            view_logger.debug("DEALER VIEW : Get Inventory request for %s through POST method"%request.user)
            if not request.user.is_authenticated():
                view_logger.debug("DEALER VIEW : Invalid session for %s"%request.user)
                result = {"status": "failure", "msg" : "Invalid session"}
            else:
                result = util.fetchInventoryData(request.user)
                view_logger.debug("DEALER VIEW : Get Inventory response for %s is %s"%(request.user, str(result)))
            return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
        return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

def update_inventory(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'GET':
            view_logger.debug("DEALER VIEW : Update inventory request for %s through GET method"%request.user)
            if not request.user.is_authenticated():
                view_logger.debug("DEALER VIEW : Redirected %s to login from update inventory"%request.user)
                return redirect('/dealer/login/')
            t = get_template('updateinventory.html')
            identifier = request.GET['identifier']
            context_dictionary = util.getInventoryData(identifier, request.user)
            context_dictionary['user'] = request.user
            html = t.render(context_dictionary)
            view_logger.debug("DEALER VIEW : Rendered Update Inventory page for : %s with context : %s"%(request.user, str(context_dictionary)))
            return HttpResponse(html)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
        return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

def jobcard_home(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'GET':
            view_logger.debug("DEALER VIEW : Job card home request for %s through GET method"%request.user)
            if not request.user.is_authenticated():
                view_logger.debug("DEALER VIEW : Redirected %s to login from Job card home"%request.user)
                return redirect('/dealer/login/')
            user_agent = "all"
            user_agent=request.META.get("HTTP_USER_AGENT")
            view_logger.debug("USER AGENT : %s"%user_agent)
            if "Android" in user_agent:
                user_agent = "android"
            t = get_template('jobcardhome.html')
            html = t.render({'user': request.user,'user_agent': user_agent})
            view_logger.debug("DEALER VIEW : Rendered Get Job card page for : %s"%request.user)
            return HttpResponse(html)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
        return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

def jobcard_new(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'GET':
            view_logger.debug("DEALER VIEW : Create job card request for %s through GET method"%request.user)
            if not request.user.is_authenticated():
                view_logger.debug("DEALER VIEW : Redirected %s to login from Create job card"%request.user)
                return redirect('/dealer/login/')
            t = get_template('createjobcard.html')
            user_agent = "all"
            user_agent=request.META.get("HTTP_USER_AGENT")
            view_logger.debug("USER AGENT : %s"%user_agent)
            if "Android" in user_agent:
                user_agent = "android"
            context_dictionary = util.getCarBrands()

            print("context_dictionary - %s" % context_dictionary)

            context_dictionary['user'] = request.user
            context_dictionary['user_agent'] = user_agent

            context_dictionary['serviceTypes'] = global_constants.service_types_dropdown
            html = t.render(context_dictionary)
            view_logger.debug("DEALER VIEW : Rendered Create job card page for : %s"%request.user)
            return HttpResponse(html)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
        return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def jobcard_edit(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'GET':
            view_logger.debug("DEALER VIEW : Edit job card request for %s through GET method"%request.user)
            if not request.user.is_authenticated():
                view_logger.debug("DEALER VIEW : Redirected %s to login from Edit job card"%request.user)
                return redirect('/dealer/login/')
            t = get_template('editjobcard.html')
            jc_id = request.GET['jc']
            view_logger.debug("DEALER VIEW : Dealer id: %s Job card id: %s"%(request.user, jc_id))
            user_agent = "all"
            user_agent=request.META.get("HTTP_USER_AGENT")
            view_logger.debug("USER AGENT : %s"%user_agent)
            if "Android" in user_agent:
                user_agent = "android"
            context_dictionary = util.getJobCard(jc_id, request.user)['jobcard_details']
            context_dictionary['user'] = request.user
            context_dictionary['user_agent'] = user_agent
            html = t.render(context_dictionary)
            view_logger.debug("DEALER VIEW : Rendered Edit Job card page for : %s with context : %s"%(request.user, str(context_dictionary)))
            return HttpResponse(html)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}

    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
        return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def generate_invoice(request):
   try:
        view_logger = log_rotator.view_logger()
        if request.method == 'GET':
            view_logger.debug("DEALER VIEW : Invoice page request for %s through GET method"%request.user)
            if not request.user.is_authenticated():
                view_logger.debug("DEALER VIEW : Redirected %s to login from Invoice page"%request.user)
                return redirect('/dealer/login/')
            t = get_template('generateinvoice.html')
            context_dictionary = {'jobcards' : util.getJobCardsList(request.user, for_invoice=True)}
            context_dictionary['user'] = request.user
            html = t.render(context_dictionary)
            view_logger.debug("DEALER VIEW : Rendered Invoice page for : %s with context : %s"%(request.user, str(context_dictionary)))
            return HttpResponse(html)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}

   except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
        return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

def view_invoice(request):
   try:
        view_logger = log_rotator.view_logger()
        if request.method == 'GET':
            view_logger.debug("DEALER VIEW : View Invoice page request for %s through GET method"%request.user)
            if not request.user.is_authenticated():
                view_logger.debug("DEALER VIEW : Redirected %s to login from View Invoice page"%request.user)
                return redirect('/dealer/login/')
            t = get_template('invoice.html')
            jc_id = request.GET['jc']
            view_logger.debug("DEALER VIEW : Dealer id: %s Job card id: %s"%(request.user, jc_id))
            context_dictionary = util.getJobCard(jc_id, request.user, True)
            html = t.render(context_dictionary)
            view_logger.debug("DEALER VIEW : Rendered View Invoice page for : %s with context : %s"%(request.user, str(context_dictionary)))
            return HttpResponse(html)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}

   except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
        return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")



