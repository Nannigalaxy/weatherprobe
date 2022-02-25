class Config:
	TIMEOUT = 10
	API_KEY = '491a8fa9fd32001343f62a66723cf13a'
	UNITS_TYPE = "metric"

	BASE_URL = 'https://api.openweathermap.org/data/2.5/onecall?'
	LOCATION_URL = 'http://api.openweathermap.org/geo/1.0/direct?q={0}&limit=1'

	APPID = "&appid={0}".format(API_KEY)
	UNITS = "&units={0}".format(UNITS_TYPE)
	LOCATION = "lat={0}&lon={1}"
	PLACE="q={0}"
	DATE="&dt={0}"



