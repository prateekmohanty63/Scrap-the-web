from itertools import tee
import json
from urllib import response
import requests
from bs4 import BeautifulSoup
import urllib3

# url ="https://www.phonepe.com/pulse/explore/transaction/2022/1/rajasthan/"
json_file_path="https://github.com/PhonePe/pulse/blob/master/data/aggregated/transaction/country/india/2018/1.json"


# r=requests.get(url)
# htmlContent=r.content
# print(htmlContent)


# response=requests.get(url1)
# print(response.json())


# with open(json_file_path, 'r') as j:
#      contents = json.loads(j.read())
#      print(contents)


response = urllib3.urlopen(json_file_path)
data = json.loads(response.read())
print(data)

# resp = requests.get(url=url1)
# data = resp.json()
# print(data)

