# tjanse_liste.py
tjanser = {
	'mokost': {
	'madhold':['10:00','10:30'],
	'opvask':['10:45','11:45'],
	'borde_gulve':['11:00','11:30'],
	},
	'aftensmad': {
	'madhold':['17:00','18:30'],
	'opvask':['17:45','18:45'],
	'borde_gulve':['18:00','18:30']
	},
	'oprydning': {
	'21:45 Oprydning': ['21:45','22:00']
	}
}
"""
tjanser = {
	'morgenmad': {
	'madhold':['08:30','10:00'],
	'opvask':['09:30','10:30'],
	'borde_gulve':['09:30','10:00'],
	},
	'frokost': {
	'madhold':['12:00','13:30'],
	'opvask':['13:00','14:00'],
	'borde_gulv':['13:00','13:30']
	},
	'aftensmad': {
	'madhold':['17:30','19:00'],
	'opvask':['18:30','19:30'],
	'borde_gulve':['18:30','19:00']
	},
	'oprydning': {
	'21:45 Oprydning': ['21:45','22:00']
	}
}

for måltid, value in tjanser.items():
	for tjans, tidspunkt in value.items():
		print("{} - {} :::: {} -- {}".format(måltid, tjans, tidspunkt[0], tidspunkt[1]))
"""