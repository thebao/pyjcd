"""
Module containing classes for HTTP client/server interactions
"""

# Python 2.x/3.x compatibility imports
try:
    from urllib.error import HTTPError, URLError
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import HTTPError, URLError
    from urllib import urlencode

import socket
from pyjcd.configuration import API_ROOT_URL
from pyjcd.exceptions import APICallError

class JCDHTTPClient(object):

    def __init__(self, API_key):
        self.API_key = API_key
        self.API_root_URL = API_ROOT_URL

    def call_API(self, API_endpoint_URL, params_dict,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
     
        url = self._build_full_URL(API_endpoint_URL, params_dict)
        errors = []
        try:
            try:
                from urllib.request import urlopen
            except ImportError:
                from urllib2 import urlopen
            response = urlopen(url, None, timeout)
        except HTTPError as e:
            raise APICallError(e)
        except URLError as e:
            raise APICallError(e)
        else:
            data = response.read().decode('utf-8')
            return data

    def _build_full_URL(self, API_endpoint_URL, params_dict):
      
        url =self.API_root_URL + API_endpoint_URL
        params = params_dict.copy()
        if self.API_key is not None:
            params['apiKey'] = self.API_key
        return self._build_query_parameters(url, params)

    def _build_query_parameters(self, base_URL, params_dict):
        return base_URL + '?' + urlencode(params_dict)

    def __repr__(self):
        return "<%s.%s>" % \
            (__name__, self.__class__.__name__)
