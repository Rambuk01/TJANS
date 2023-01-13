# date_test.py
import datetime
date = datetime.datetime.now()
date_string = date.strftime("%d-%m-%Y")

def three_days(d=date):
	friday = d.strftime("%d-%m-%Y")
	temp = d + datetime.timedelta(days=1)
	saturday = temp.strftime("%d-%m-%Y")
	temp = d + datetime.timedelta(days=2)
	sunday = temp.strftime("%d-%m-%Y")
	return [friday, saturday, sunday]

