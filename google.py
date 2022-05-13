import urllib.request, json 
with urllib.request.urlopen("https://www.phonepe.com/data/aggregated/transactions/country/india/2018/1.json") as url:
    data = json.loads(url.read().decode())
    print(data)