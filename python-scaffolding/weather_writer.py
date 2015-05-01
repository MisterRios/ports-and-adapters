
class WeatherApp:

	def __init__(self, weather_adaptor, csv_adaptor):
	    
	    self.weather_adaptor = weather_adaptor
	    self.csv_adaptor = csv_adaptor

	def weather_translator(self):

		results = self.weather_adaptor.api_adapter()['results']



		for result in results:
			headers = ['id','name','date','time','temperature','pressure','wind_direction']
			

			id = result['id']
			name = result['name']
			date,time = result['time'].split()
			temperature = result['TD']
			pressure = result['P']
			wind_direction = result['D']



			line = ",".join(id,name,date,time,temperature,pressure,wind_direction)
			
			csv_adaptor.write(line)

		

