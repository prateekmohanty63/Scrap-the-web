import json
from urllib.request import urlopen

with urlopen('https://github.com/PhonePe/pulse/blob/master/data/aggregated/transaction/country/india/2019/1.json') as response:
  data = response.read()

print(data)