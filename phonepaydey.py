import json
from urllib.request import urlopen

import requests
 
url = 'https://raw.githubusercontent.com/PhonePe/pulse/master/data/aggregated/transaction/country/india/2019/1.json'
resp = requests.get(url)
data = json.loads(resp.text)
print(data)