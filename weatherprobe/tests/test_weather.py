from weather_api.weather import WeatherData
import unittest


class TestWeatherAPI(unittest.TestCase):

	def test_weatherdata(self):
		self.assertEqual(WeatherData(date='2022-02-26', time='20:04').hourly(), None)
		self.assertTrue(WeatherData(date='2022-02-26', time='20:04', place='bangalore').hourly(), True)
		self.assertTrue(WeatherData(date='2022-02-26', time='20:04', longitude='12', latitude='75').hourly(), True)

