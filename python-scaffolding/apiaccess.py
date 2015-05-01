__author__ = 'hschmeisky'

import requests, json
import pprint

def api_adapter():
	url = 'http://apis.is/weather/observations/en?stations=1'
	response = requests.get(url)
	
	return json.loads(response.content)

if __name__ == '__main__':
	
	pprint.pprint(api_adapter())