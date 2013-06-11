from configuration import *
from utils import make_request, APIError

class EverybitAPI():

    def __init__(self):
        pass

    def get_account_info(self):
        """
        Get user's account info.
        """
        
        url = '%s/v1/account' % api_base_url
        return make_request(url)

    def get_videos(self, uuid=None):
        """
        Get videos for this user.

        If there is a uuid provided, we'll retrieve a single video's details.
        If there is no uuid, it will get all the videos in the user's account.
        """

        url = '%s/v1/videos' % api_base_url
        if uuid:
            url = '%s/%s' % (url, uuid)
        return make_request(url)

    def create_video(self, json_data=None):
        """
        Create a new video.

        Will throw an APIError if there is no json_data present.
        """

        if not json_data:
            raise APIError("You must provide a uuid to update a video.")

        url = '%s/v1/videos' % api_base_url
        return make_request(url, 'POST', json_data)

    def update_video(self, uuid=None, json_data=None):
        """
        Update an existing video.

        A uuid and some json data (dict) are required here.
        """

        if not uuid:
            raise APIError("You must provide a uuid to update a video.")
        if not json_data:
            raise APIError("You must provide a uuid to update a video.")

        url = '%s/v1/videos' % api_base_url
        url = '%s/%s' % (url, uuid)
        return make_request(url, 'PUT', json_data)

    def get_video_status(self, uuid=None):
        """
        Get the video's status.

        If the video is currently encoding, we can see how far along it is.
        If the video is done encoding, or there was an error, we can find that
        out here as well.
        """

        if not uuid:
            raise APIError("You must provide a uuid to update a video.")

        url = '%s/v1/videos/%s/status' % (api_base_url, uuid)
        return make_request(url, 'GET')