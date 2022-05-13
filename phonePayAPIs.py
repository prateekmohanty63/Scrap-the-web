import json
from urllib.request import urlopen

import requests
 
# getting data of all states
url = 'https://raw.githubusercontent.com/PhonePe/pulse/master/data/map/user/hover/country/india/2018/1.json'
# resp = requests.get(url)
# data = json.loads(resp.text)
# print(data)


# getting data of all districts of a particular state

url = 'https://raw.githubusercontent.com/PhonePe/pulse/master/data/map/user/hover/country/india/state/karnataka/2018/1.json'
resp=requests.get(url)
data=json.loads(resp.text)
print(data)