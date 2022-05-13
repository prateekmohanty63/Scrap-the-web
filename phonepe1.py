import json
  
# Opening JSON file
f = open('https://github.com/PhonePe/pulse/blob/master/data/aggregated/transaction/country/india/2018/1.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
print(data)
  
# Iterating through the json
# list

  
# Closing file
f.close()