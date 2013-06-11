#!/usr/bin/python

from everybit import *


test_uuid = '4d8505a0-89c9-431c-9e85-2e3776837a15'
Everybit = EverybitAPI()

print "### Getting account info for user '%s'" % api_key
print Everybit.get_account_info()

print "### Getting video details for '%s' ###" % test_uuid
print Everybit.get_videos(test_uuid)

print "### Getting video details for all videos ###"
print Everybit.get_videos()

print "### Updating video '%s' ###" % test_uuid
json_data = {
    "title": "video title", "summary": "short summary or description of video",
    "tags": ["terms", "describing", "video"], "lat": 42.000, "lon": 41.000,
    "visibility": "public"
}
print Everybit.update_video(test_uuid, json_data)

print "### Creating new video ###"
json_data = {
    "title": "video title", "summary": "short summary or description of video",
    "visibility": "public", "lat": float(52.000), "lon": float(51.000),
    "source_file": "http://www.moovatom.com/static/clips/big_buck_bunny_clip_1.mov",
    "callback_url": "http://www.moovatom.com/api/v2/callback-test"
}
print Everybit.create_video(json_data)

print "### Getting video status for '%s' ###" % test_uuid
print Everybit.get_video_status(test_uuid)