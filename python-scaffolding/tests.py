import unittest
import weather_writer


class TestTheCSVWeather(unittest.TestCase):

	def test_get_weather_write_csv(self):

		data_to_write = weather_writer.writer()
		self.assertEquals(type(data_to_write), list)


if __name__ == '__main__':
	unittest.main()