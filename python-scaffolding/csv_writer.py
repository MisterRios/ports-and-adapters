
headers = ['id','name','date','time','temperature','pressure','wind_direction']

def write(line):
	with open('weather_data.csv', 'w+') as csv_file:
		csv_file.write_line(line)

