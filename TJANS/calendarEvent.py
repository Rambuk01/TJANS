import requests
from getcookie import *

def create_calendar_event(headline='hej', description='meddig', startdate=0, starttime='18:00', enddate=0, endtime='18:30', studentid=""):
	url = 'https://nordborgslot.viggo.dk/Shared/Events/SaveEvents'
	#headers = {'cookie':'.AspNetCore.Session={}'.format(cookies)}
	#heads = {'cookie':'ViGGO.Session=80e699d7-9d63-482d-aebe-81584d9bd568'}
	headers = {'cookie':'.AspNetCore.Session={}'.format("CfDJ8AC8GJmEkQFCh3E89ILer/w6drTmSEvOTQ4LkJ7PomeJLWoSzVm6Wm59k3Q3CEVTKLnAqurwKelqbCAmb0Ls/gIGwY2SAuuXGvrayZ6trzHmc1B6vxJoF1VssV6Ivle7RwbHIVM/AJ6QONgAx8uC4E4AbxaMs7hN5OKF82hQNR0o")}

	data = {
	'Headline': headline,
	'Description': description,
	'Cal endarId': 0,
	'refCalendarPremisesId': 0,
	'startdate': '{}'.format(startdate),
	'starttime': '{}'.format(starttime),
	'enddate': '{}'.format(enddate),
	'endtime': '{}'.format(endtime),
	'periodstart': '03-11-2020',
	'periodend': '03-02-2021',
	'ClientCalendarId': 13,
	'Users': '{}'.format(studentid) #2756 er mit
	}
	print(headers)
	x = requests.post(url, data = data, headers = headers)
	print(x.text)

#create_calendar_event(startdate=date_string, starttime='18:00', enddate=date_string, endtime='20:30', teacher=2756)

"""
data = {
'Headline': 'Something something',
'Description': 'Nyt nyt',
'Cal endarId': 0,
'refCalendarPremisesId': 0,
'startdate': '09-11-2020',
'starttime': '19:50',
'enddate': '09-11-2020',
'endtime': '20:25',
'periodstart': '03-11-2020',
'periodend': '03-02-2021',
'ClientCalendarId': 7,
'Users': '2756'
}
"""

"""
IsPrivate: 
Headline: ASD
Description: <p>DSA</p>
CalendarId: 0
Note: 
refCalendarPremisesId: 0
startdate: 03-11-2020
starttime: 15:50
enddate: 03-11-2020
endtime: 19:25
PremisesId: 0
periodstart: 03-11-2020
periodend: 03-02-2021
ClientCalendarId: 6
Groups: 
Users: 2756
"""

