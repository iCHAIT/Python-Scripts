import requests
import json
from random import randint
import urllib

# Timestamp for 11 July in UTC
timeStamp = 1436553000

# Generate access token here: https://developers.facebook.com/tools/explorer/
accessToken = ' <insert token here> KEEP the quotes'

query = " SELECT post_id, actor_id, created_time, message FROM stream WHERE \
                filter_key = 'others' AND source_id = me() AND \
                created_time > " + str(timeStamp) + " LIMIT 200 "

wishes = {'access_token': accessToken, 'q': query}
r = requests.get('https://graph.facebook.com/fql', params=wishes)
result = json.loads(r.text)
wallposts = result['data']


print str(len(wallposts)) + " to handle"
base = "https://graph.facebook.com/"
count = 1
for wallpost in wallposts:
    checkWish = wallpost['message'].split()
    if set(['happy', 'happiee', 'hbd', 'HBD', 'bday', 'birthday', 'returns']).intersection(set(checkWish)) > 0:
        url = base + '%s/comments' % wallpost['post_id']
        likes = base + str(wallpost['post_id']) + "/likes/?access_token=" + accessToken + "&method=POST"
        commented = base + str(wallpost['post_id']) + "/comments/?access_token=" + accessToken + "&method=GET"
        post_comments = urllib.urlopen(commented)
        jsonSource = post_comments.read()
        post_comments.close()
        requests.post(likes)
        messages = ['Thank you :)', 'Thanks :)']
        comment = {'access_token': accessToken, 'message': messages[randint(0, 1)]}
        if len(jsonSource) == 11:   # Find a neater way to handle this.
            requests.post(url, data=comment)
        print "Wall post %d done" % count
        count += 1
