import json

import urllib.request
import requests
from urllib.request import urlopen


import urllib3

url="https://github.com/PhonePe/pulse/blob/master/data/aggregated/transaction/country/india/2019/1.json"


# response = urlopen(url)

# data = json.loads(response.read())

# print(data)


r = requests.get(url,headers={'accept': 'application/json'})
print (r.content)

# json_url = urlopen(url)

# data = json.loads(json_url.read())

# print (data)