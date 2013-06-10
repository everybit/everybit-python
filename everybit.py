
from configuration import *
from utils import make_request, APIError, APIConnectionError

class EverybitAPI():

    def __init__(self):
        pass

    def get_account_info(self):
        url = '%s/v1/account' % api_base_url
        resp = make_request(url)
        return resp

    def get_videos(self, uuid=None):
        url = '%s/v1/videos' % api_base_url
        if uuid:
            url = '%s/%s' % (url, uuid)
        resp = make_request(url)
        return resp

    def create_video(self, args):
        url = '%s/v1/videos' % api_base_url
        resp = make_request(url, 'POST', args)
        return resp
        
    def update_video(self, args, uuid=None):
        url = '%s/v1/videos' % api_base_url
        if not uuid:
            raise APIError("You must provide a uuid to update a video.")
        url = '%s/%s' % (url, uuid)
        resp = make_request(url, 'PUT', args)
        return resp

    def get_video_status(self, uuid=None):
        url = '%s/v1/videos' % api_base_url
        if not uuid:
            raise APIError("You must provide a uuid to update a video.")
        url = '%s/%s/status' % (url, uuid)
        resp = make_request(url, 'GET')
        return resp