__author__ = 'hschmeisky'

import requests, json

url = 'http://apis.is/weather/observations/en?stations'r
response = requests.get(url)
print json.loads(response.content)