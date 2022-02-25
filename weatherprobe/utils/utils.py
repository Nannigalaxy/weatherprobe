from datetime import datetime
import inspect

curfunc = lambda: inspect.stack()[2][3]

def time_now():
	return datetime.now().strftime("%H:%M")

def date_now():
	return datetime.now().strftime("%Y-%m-%d")