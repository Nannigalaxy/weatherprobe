import logging
import datetime
import time
import requests
from weather_api.config import Config
import ast

conf = Config

class WeatherData:
	""" Weather Data from API """
	def __init__(self, date, time, latitude=None, longitude=None, place=None):
		self.date = date
		self.time = time
		self.longitude = longitude
		self.latitude = latitude
		self.place = place

	def get_unix_time(self):
		""" Convert date time to unix time """
		date_t = map(int, self.date.split('-'))
		time_t = map(int, self.time.split(':'))
		date_time = datetime.datetime(*date_t, *time_t)
		unix_time = int(time.mktime(date_time.timetuple()))
		return unix_time

	def parse_dict(self, data):
		""" Parse required data from API response """
		report = dict()
		date_time = datetime.datetime.fromtimestamp(data['dt'])
		report['Date Time'] = (f"{date_time:%Y-%m-%d %H:%M:%S}", "")
		report['Humidity'] = (data['humidity'], "%")
		report['Pressure'] = (data['pressure'], "hPa")
		report['Average Temp.'] = (data['temp'], "°C")
		report['Wind Speed'] = (data['wind_speed'], "m/s")
		report['Wind degree'] = (data['wind_deg'], "degrees")
		report['UV Index'] = (data['uvi'], "")
		return report

	def api_request(self, url):
		""" Request query and return report """
		response = requests.get(url, timeout=conf.TIMEOUT)
		if response.status_code == 200:
			data = response.content.decode('utf-8')
			raw_dict = ast.literal_eval(data)
			return raw_dict
		else:
			return False

	def fetch_report(self):
		""" Fetch location weather report """
		try:
			if self.place and not (self.latitude or self.longitude):
				url = conf.LOCATION_URL.format(self.place)+conf.APPID+conf.UNITS
				raw_dict = self.api_request(url)
				if raw_dict:
					self.latitude, self.longitude = raw_dict[0]['lat'], raw_dict[0]['lon']

			unix_time = str(self.get_unix_time())

			url = conf.BASE_URL+conf.LOCATION.format(self.latitude, self.longitude)+conf.DATE.format(unix_time)+conf.APPID+conf.UNITS
			raw_dict = self.api_request(url)
			if raw_dict:
				return raw_dict

		except Exception as e:
			logging.error(e)
			return False


	def hourly(self):
		""" Get closest successive hour weather report """
		report = self.fetch_report()
		if report:
			unix_time = self.get_unix_time()
			index = -1
			data = dict()
			data['lon'] = report['lon']
			data['lat'] = report['lat']
			data['hourly'] = report['hourly']
			for i in range(len(data['hourly'])):
				if data['hourly'][i]['dt']>unix_time:
					index = i
					break
			if index>-1:
				data['required'] = data['hourly'][index]
				data['report'] = self.parse_dict(data['required'])
				return data

			else:
				return False
