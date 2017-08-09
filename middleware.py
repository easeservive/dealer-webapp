from django.utils.html import escape
from django.core.urlresolvers import reverse
from django.http import HttpResponse

import log_rotator
import datetime


class TrackingMiddleware(object):
    """
    Visitor tracking and logging Middleware class.
    """
    empty_response = 'NA'

    def process_request(self, request):
        try:
            request_time = datetime.datetime.now()
            request.__setattr__('request_time', request_time)
        except:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            pass

    def get_log_record_response_str(self, response, request, request_time):
        """
        Creates and returns a string based on a defined format to be logged in the response log.
        Format for the string is as specified below with '|'(pipe) as delimiter:
        """
        request_obj = response.get('_request', request)
        ip = request_obj.META.get('REMOTE_ADDR', self.empty_response)
        status = response.status_code
        url = str(request_obj.META.get('PATH_INFO'))
        method = request_obj.META.get('REQUEST_METHOD', self.empty_response)
        response_time = datetime.datetime.now()
        process_time = str(response_time - request_time)
        browser = escape(request.META.get('HTTP_USER_AGENT', self.empty_response))
        referrer = str(request.META.get('HTTP_REFERER', self.empty_response))
        if('session' in request_obj) and ('user' in request_obj.session):
            user = request_obj.session.get('user')
        else:
            user = self.empty_response
        ios_version = escape(request.META.get('HTTP_IOSVERSION', self.empty_response))
        android_version = escape(request.META.get('HTTP_ANDROIDVERSION', self.empty_response))
        # record_str = '%(request_time)s | %(status)s | %(method)s | %(ip)s | %(url)s | %(process_time)s | %(ios_version)s' % {'status': status, 'method': method, 'ip': ip, 'url': url,'process_time':process_time,'request_time':request_time, 'ios_version': ios_version}
        # return record_str
        record_dict = {'status': status, 'method': method, 'ip': ip, 'url': url, 'process_time': process_time, 'request_time': request_time, 'ios_version': ios_version,
                       'response_time': response_time, 'browser': browser, 'referrer': referrer, 'user': user, 'android_version': android_version}
        return record_dict

    def process_response(self, request, response):
        try:
            request_time = request.request_time if hasattr(request, 'request_time') else datetime.datetime.now()
            record_dict = self.get_log_record_response_str(response, request, request_time)
            record_str = '%(request_time)s | %(status)s | %(method)s | %(ip)s | %(url)s | %(process_time)s | %(browser)s | %(referrer)s | %(user)s | %(ios_version)s | %(android_version)s' % record_dict
            tracking_logger = log_rotator.tracking_logger()
            tracking_logger.debug(record_str)
        except:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
        return response

    def process_exception(self, request, exception):
        try:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception ::", exc_info=True)
        except:
            pass
