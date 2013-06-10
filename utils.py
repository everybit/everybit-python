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


## Request Helpers
def make_request(url, http_verb='GET', json_data={}):

    try:
        if http_verb=='POST':
            return post(url, json_data)
        else:
            data = json.dumps(json_data)
        print "Calling: %s with: %s and data: %s" % (url, http_verb, data)
        req = urllib2.Request(
            url,
            data,
            {
                'x-apikey': api_key
            }
        )
        req.get_method = lambda: http_verb
        f = urllib2.urlopen(req)
        response = f.read()
        f.close()
        print response
        return response
    except Exception, e:
        print "Exception making request: %s" % e
        return None

def post(url, json_data):
    try:
        params = urllib.urlencode(json_data)
        params = json.dumps(json_data)
        response = urllib2.urlopen(
            url,
            params,
            {
                'x-apikey': api_key
            }
        )
        response = response.read()
        print response
        return response
    except Exception, e:
        print "Exception making request: %s" % e
