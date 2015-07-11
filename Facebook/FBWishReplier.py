import requests
import json
from random import randint
import urllib

# http://www.timestampgenerator.com/
# Use this link to generate the timeStamp.
timeStamp = 1436553000

# Initialize the Graph API with a valid access token
# Generate access token here: https://developers.facebook.com/tools/explorer/
accessToken = 'CAACEdEose0cBAMbbl879eFiRRBZC6fEJ0Cllnkp7nHz1PNtPnmb0UYKWbKFMVgjobbMvTOCU80SKyx7l9bys8kAFb3MZCSsBCkn9GDWPNaaUfZCTmYRDedt2QcnwYRfOrVc3EZANBo6OgTdVK1TotQrnxjM3olDqRtSZAuCRBpBm6ZCZAg0KhhsK9IMcYJDjVR70R1AacZAChcjcy6sQxGx3aZBnHPcFSjQ0ZD'

query = " SELECT post_id, actor_id, created_time, message FROM stream WHERE \
                filter_key = 'others' AND source_id = me() AND \
                created_time > " + str(timeStamp) + " LIMIT 200 "

wishes = {'access_token': accessToken, 'q': query}
r = requests.get('https://graph.facebook.com/fql', params=wishes)
result = json.loads(r.text)
wallposts = result['data']


print str(len(wallposts)) + " to handle"
baseUrl = "https://graph.facebook.com/"
count = 1
for wallpost in wallposts:
    forCheck = wallpost['message'].split()
    if set(['happy', 'happiee', 'hbd', 'HBD', 'bday', 'birthday', 'returns']).intersection(set(forCheck)) > 0:
        url = baseUrl + '%s/comments' % wallpost['post_id']
        likesUrl = baseUrl + str(wallpost['post_id']) + "/likes/?access_token=" + accessToken + "&method=POST"
        commented = baseUrl + str(wallpost['post_id']) + "/comments/?access_token=" + accessToken + "&method=GET"
        post_comments = urllib.urlopen(commented)
        htmlSource = post_comments.read()
        post_comments.close()
        requests.post(likesUrl)
        messages = ['Thank you :)', 'Thanks :)']
        comment = {'access_token': accessToken, 'message': messages[randint(0,1)]}
        if len(htmlSource) == 11:
            requests.post(url, data=comment)
        print "Wall post %d done" % count
        count += 1
