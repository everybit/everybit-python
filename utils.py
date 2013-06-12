import urllib
import urllib2
import json

from configuration import *


## Exceptions
class EverybitError(Exception):
  def __init__(self, message=None, http_body=None, http_status=None, json_body=None):
    super(EverybitError, self).__init__(message)
    self.http_body = http_body and http_body.decode('utf-8')
    self.http_status = http_status
    self.json_body = json_body

class APIError(EverybitError):
  pass

class APIConnectionError(EverybitError):
  pass


class EverybitRequest(urllib2.Request):
    """
    Override the urllib2 Request so we can easily set the method.
    """

    def __init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False, method=None):
       urllib2.Request.__init__(self, url, data, headers, origin_req_host, unverifiable)
       self.method = method

    def get_method(self):
        if self.method:
            return self.method

        return urllib2.Request.get_method(self)


def make_request(url, method='GET', data={}):
    """
    Convenience function for building requests
    """

    try:
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        req = EverybitRequest(
            url,
            data=json.dumps(data),
            headers={
                'User-Agent': api_user_agent,
                'x-apikey': api_key
            },
            method=method,
        )
        return opener.open(req).read()
    except Exception, e:
        raise APIConnectionError(
            message="It appears we were unable to communicate with the Everybit API.  Is your API key set?  Are you passing in correctly formatted data? %s" % e
        )
