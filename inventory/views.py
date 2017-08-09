
# Create your views here.
import json
import datetime

from django.http import HttpResponse

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

def auto_suggest_inventory(request):
    try:
        if request.method == 'POST':
            if request.user.is_authenticated():
                result = util.fetchInventoryData(request.user)
            else:
                result = {"status": "unauthorized", "msg": "Not authorized."}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")

def updateStocks(request):
    try:
        if request.method == 'POST':
            if request.user.is_authenticated():
                data = request.POST
                details = {}
                details['brand'] = data['brand']
                details['model'] = data['model']
                details['identifier'] = data['identifier']
                details['description'] = data['description']
                details['ndp'] = data['ndp']
                details['mrp'] = data['mrp']
                details['min_qty'] = data['min_qty']
                details['avail_qty'] = data['avail_qty']
                details['critical'] = data.get('critical', '0')
                details['alternate'] = data.get('alternate', '0')
                result = util.updateInventoryItem(details, request.user)
            else:
                result = {"status": "unauthorized", "msg": "Not authorized."}
        else:
            result = {"status": "failure", "msg": "Invalid request method"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "something went wrong"}
    return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")


