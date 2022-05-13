
import json
from urllib.request import urlopen
import urllib.request
import requests


import urllib3
# with urllib.request.urlopen("https://github.com/PhonePe/pulse/blob/master/data/aggregated/transaction/country/india/2018/1.json") as url:
#     data = json.loads(url.read())
#     print(data)


# json_file_path='https:\\github.com\\PhonePe\\pulse\\blob\\master\\data\\aggregated\\transaction\\country\\india\\2018\\1.json'
# with open("https://github.com//PhonePe//pulse//blob//master//data//aggregated//transaction//country//india//2018//1.json","r") as j:
#     data=j.read()
#     print(data)
     
# json_file_path='https:\\github.com\\PhonePe\\pulse\\blob\\master\\data\\aggregated\\transaction\\country\\india\\2018\\1.json'
# with open('https://github.com//PhonePe//pulse//blob//master//data//aggregated//transaction//country//india//2018//1.json','r') as j:
#     json_load = json.load(j)
# print(json_load)


# with urllib.request.urlopen("http://github.com/PhonePe/pulse/blob/master/data/aggregated/transaction/country/india/2018/1.json") as j:
#     json_load = json.load(j.decode('utf-8'))
# print(json_load)

url="http://github.com/PhonePe/pulse/blob/master/data/aggregated/transaction/country/india/2018/1.json"
# resp_text = urllib.request.urlopen(url).read().decode('UTF-8')
# # Use loads to decode from text
# json_obj = json.loads(resp_text)
# print(requests.get(url).content)

data=requests.get(url).json()
print(data)

     