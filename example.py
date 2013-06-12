#!/usr/bin/python

import json
import time

from everybit.api import *


Everybit = EverybitAPI()


################################################################################
#Get user account info
print "### Getting account info for user '%s'" % api_key
print Everybit.get_account_info()


################################################################################
#Create a video
print "### Creating new video ###"
data = {
    'title': 'Video Title', 'summary': 'Short summary or description of video',
    'visibility': 'public', 'lat': 52.1234, 'lon': 51.4311,
    'source_url': 'http://www.moovatom.com/static/clips/big_buck_bunny_clip_1.mov',
    'callback_url': 'http://www.moovatom.com/api/v2/callback-test'
}
json_data = json.loads(Everybit.create_video(data))
print json_data
uuid = json_data["data"]["uuid"]


################################################################################
#Get the video status for the video we just created
print "### Getting video status for '%s' ###" % uuid
time.sleep(5)
print Everybit.get_video_status(uuid)
time.sleep(5)
print Everybit.get_video_status(uuid)


################################################################################
#Get video details for the video we just created
print "### Getting video details for '%s' ###" % uuid
print Everybit.get_videos(uuid)


################################################################################
#Get the video details for all videos
print "### Getting video details for all videos ###"
print Everybit.get_videos()


################################################################################
#Update the video we just created with new data
print "### Updating video '%s' ###" % uuid
data = {
    'title': 'Updated Video Title', 'summary': 'Another description of video',
    'tags': ["terms", "describing", "video"], 'lat': 42.8765, 'lon': 41.7657,
    'visibility': 'public'
}
print Everybit.update_video(uuid, data)
