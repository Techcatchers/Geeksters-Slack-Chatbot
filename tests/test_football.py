import http.client
import json
import sys
sys.path.append('D:/Web Development and Programming/TCS Inframind/Slackbot Prototype/src')
from football import live_football

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'd8c3e3808b4e445cb2755783d7d05d43' }
connection.request('GET', '/v2/matches?status=LIVE&competitions=2021,2016,2019,2017,2140', None, headers )
# connection.request('GET', '/v2/matches?status=LIVE', None, headers )
# connection.request('GET', '/v2/competitions', None, headers )
response = json.loads(connection.getresponse().read().decode())

# print (response)
print(json.dumps(response, indent=4, sort_keys=True))

count = 0
while True:
    try:
        print(response["matches"][count]["competition"])
        count += 1
    except:
        break

print(count)

comp_set = {'la liga', 
            'premier league', 
            'championship', 
            'serie a', 
            'primeira liga'}
            
print(live_football(comp_set))