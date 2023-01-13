# test_calendar_event.py
import requests
url = 'https://nordborgslot.viggo.dk/Shared/Events/SaveEvents'
#heads = {'cookie':'ViGGO.Session={}'.format(cookies)}
heads = {'cookie':'ViGGO.Session=661bcc33-3dab-4c9a-b303-c9e595dfe2e0'}
d = {
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
print(heads)
x = requests.post(url, data = d, headers = heads)
print(x.text)