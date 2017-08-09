import json
import datetime

from django.http import HttpResponse
#import simplejson
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


def addvehicle(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'POST':
            data = request.POST
            v_type = data.get('type', 'NA')
            brand = data.get('brand', 'NA')
            model = data.get('model', 'NA')
            fuel_type = data.get('fuel_type', 'NA')
            chasis_number = data.get('c_num', 'NA')
            year_of_man = data.get('man_year', 'NA')
            reg_num = data.get('reg_num', 'NA')
            user = request.session.get('user', 'NA')
            view_logger.debug("JOBCARD VIEW : Add Vehicle Request - v_type: %s, brand: %s, model: %s, fuel_type: %s, chasis_number: %s, year_of_man: %s, reg_num: %s"%(v_type, brand, model,fuel_type,chasis_number,year_of_man,reg_num))
            vehicle = Vehicles.objects.create(VehicleType = v_type,
                                              Brand = brand,
                                              Model = model,
                                              FuelType = fuel_type,
                                              RegNumber = reg_num,
                                              YearOfManufacture = year_of_man,
                                              ChasisNumber = chasis_number,
                                              User = user)
            result = {"status": "success", "msg": "Added successfully"}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    view_logger.debug("JOBCARD VIEW : Add Vehicle Response - %s"%str(result))
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def fetch_scheduled_maintenance(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'POST':
            data = request.POST
            brand = data.get('brand', 'NA')
            model = data.get('model', 'NA')
            fuel_type = data.get('fuel_type', 'NA')
            km_ticked = int(data.get('km_ticked', '0'))
            view_logger.debug("JOBCARD VIEW : Fetch sch maint Request - brand: %s, model: %s, fuel_type: %s, km_ticked: %s"%(brand, model, fuel_type, km_ticked))
            result = util.fetchScheduledServices(brand, model, fuel_type, km_ticked)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    view_logger.debug("JOBCARD VIEW : Fetch sch maint Response - %s"%str(result))
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def estimate_parts(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'POST':
            if not request.user.is_authenticated():
                result = {"status": "failure", "msg" : "Invalid session"}
            else:
                data = request.POST
                parts = data.get('parts', 'NA')
                dealerid = request.user
                view_logger.debug("JOBCARD VIEW : Estimate parts request - parts: %s, dealerid: %s"%(str(parts), dealerid)) 
                result = util.getEstimate(parts, dealerid)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    view_logger.debug("JOBCARD VIEW : Estimate parts response - %s"%str(result))
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def fetch_job_card(request):
    try:
        view_logger = log_rotator.view_logger()
        view_logger.debug("JOBCARD GET REQQ : Fetch job card request details: %s :"%(request))
        if request.method == 'POST':
            if request.user.is_authenticated():
                data = request.POST
                jc_id = data.get('jc_id', 'NA')
                dealerid = request.user
                view_logger.debug("JOBCARD VIEW : Fetch job card request for jobcard: %s dealerid : %s"%(jc_id, dealerid))
                result = util.getJobCard(jc_id, dealerid)
            else:
                result = {"status": "failure", "msg" : "Invalid session"}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    view_logger.debug("JOBCARD VIEW : Fetch job card response - %s"%str(result))
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def create_job_card(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'POST':
            if request.user.is_authenticated():
                data = request.body
                data = json.loads(data)
                data = data['data']
                view_logger.debug("JOBCARD VIEW : Create job card request - %s"%str(data))
                dealerid = request.user
                details = {}

                details['veh_num'] = data['veh_num']
                details['brand'] = data['brand']
                details['model'] = data['model']
                details['fuel_type'] = data['fuel_type']
                details['c_num'] = data['c_num']
                details['cust_name'] = data['cust_name']
                details['cont_num'] = data['cont_num']
                details['cont_address'] = data['cont_address']
                details['km_ticked'] = data['km_ticked']

                details['del_time'] = data['del_time']
                details['status'] = data['status']
                details['reason'] = data['reason']

                details['services'] = data['services']
                details['spares'] = data['spares']
                details['otherparts_desc'] = data['otherparts_desc']
                details['otherparts_cost'] = data['otherparts_cost']
                details['recommendedservices'] = data['recommendedservices']
                details['labour_cost'] = data['labour_cost']
                result = util.createJobCard(details, dealerid)
                result['url'] = '/jobcard/'
            else:
                result = {"status": "failure", "msg" : "Invalid session"}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    view_logger.debug("JOBCARD VIEW : Create job card response - %s"%str(result))
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def save_job_card(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'POST':
            if request.user.is_authenticated():
                data = request.body
                dealerid = request.user
                details = {}

                data = json.loads(data)
                data = data['data']
                view_logger.debug("JOBCARD VIEW : Save job card request - %s"%str(data))

                details['jc_id'] = data.get('jc_id', 'NA')
                details['veh_num'] = data['veh_num']
                details['brand'] = data['brand']
                details['model'] = data['model']
                details['fuel_type'] = data['fuel_type']
                details['c_num'] = data['c_num']
                details['cust_name'] = data['cust_name']
                details['cont_num'] = data['cont_num']
                details['cont_address'] = data['cont_address']
                details['km_ticked'] = data['km_ticked']
                details['service_reminder_time'] = data['service_reminder_time']
                details['del_time'] = data['del_time']
                details['status'] = data['status']
                details['reason'] = data['reason']
                details['otherparts_desc'] = data['otherparts_desc']
                details['otherparts_cost'] = data['otherparts_cost']
                details['services'] = data['services']
                details['spares'] = data['spares']
                details['recommendedservices'] = data['recommendedservices']
                details['labour_cost'] = data['labour_cost']
                result = util.saveJobCard(details, dealerid, details['jc_id'])
                result['url'] = '/jobcard/'
            else:
                result = {"status": "failure", "msg" : "Invalid session"}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    view_logger.debug("JOBCARD VIEW : Save job card response - %s"%str(result))
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def data_for_jobs_auto_suggestion(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'POST':
            result = util.getCompliantCodes()
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def data_for_parts_auto_suggestion(request):
    try:
        view_logger = log_rotator.view_logger()
        view_logger.debug("PARTS GET REQQ : Fetch PARTS details: %s :"%(request.user))
        if request.method == 'POST' or request.method == 'GET':
            if request.user.is_authenticated():
                view_logger.debug("JOBCARD VIEW : Data for Parts suggestion request for  %s"%str(request.user))
                result = util.fetchInventoryData(request.user)
            else:
                result = {"status": "unauthorized", "msg": "Not authorized."}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    view_logger.debug("JOBCARD VIEW : Data for Parts suggestion response - %s"%str(result))
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


def generate_invoice(request):
    try:
        view_logger = log_rotator.view_logger()
        if request.method == 'POST':
            data = request.body
            dealerid = request.user
            details = {}
            view_logger.debug("JOBCARD VIEW : Generate Invoice request - %s"%str(request))
            try:            
               data = json.loads(data)
               data = data['data']
            except:
               data={} 
               data['jc_id']=request.POST.keys()[0]
               data['pmt_mode']=request.POST.values()[0]
               view_logger.debug("JOBCARD VIEW : Generate Invoice request - %s"%str(data))       
            view_logger.debug("JOBCARD VIEW : Generate Invoice request - %s"%str(data))
            jc_id = data['jc_id']
            pmt_mode = data['pmt_mode']
            result = util.generateInvoice(jc_id, pmt_mode, dealerid)
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    view_logger.debug("JOBCARD VIEW : Generate Invoice response - %s"%str(result))
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

def get_jobcards_list(request):
    try:
        view_logger = log_rotator.view_logger()
        view_logger.debug("JOBCARD VIEW : Get Job card request detail %s"%str(request.session.get('user')))
        view_logger.debug("JOBCARD VIEW : Get Job card request detail %s"%str(request))
        if request.method == 'POST':
            view_logger.debug("JOBCARD VIEW : Get Job card list request for %s"%str(request.user))
            view_logger.debug("JOBCARD VIEW : Get Job card list request for %s"%str(request.user.is_authenticated()))
            if request.user.is_authenticated():
                result = {"status": "success", "data": util.getJobCardsList(request.user)}
            else:
                result = {"status": "unauthorized", "msg": "Not authorized."}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    view_logger.debug("JOBCARD VIEW : Get Job card list response - %s"%str(result))
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


