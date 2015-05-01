import unittest
import weather_writer
import test_apiaccess



class TestTheCSVWeather(unittest.TestCase):

	def test_get_weather(self):

		# We call the API for weather information
		test_response = apiaccess.api_adapter()
		self.assertEquals(type(test_response), dict)

	def test_make_list_for_csv(self):
		# We make the data into a list

		data_to_write = weather_writer.WeatherApp(test_apiaccess, test_csv_writer)

		self.assertEquals(type(data_to_write), list)
		self.assertNotEquals(len(data_to_write), 0)

	def test_csv_outputted(self):
		# We see a csv file that has been output
		pass


if __name__ == '__main__':
	unittest.main()