# app.py
from get_weekend_id_app import *
from teacher_ids import *
from draw_function import *
from date_test import *
from tjanse_liste import *
from calendarEvent import create_calendar_event

def app():
	days = three_days(datetime.date(2022, 6, 17))
	antal_elever_pr_tjans = int(input('Hvor mange elever pr. tjans?: '))
	for day in days:
		for måltid, value in tjanser.items():
			for tjans, tidspunkt in value.items():
				"""
				# Det er ikke dag 3 og dag 2, ingen oprydning
				if day != days[2] and day != days[1]:
					if "oprydning" == måltid:
						continue
				"""
				if day == days[0]:
					if måltid == "morgenmad" or måltid == "frokost" or måltid == "mokost":
						continue
				# draw 3 users and get the 3 ids.
				if "oprydning" == måltid:
					users = draw_students(5)
				else:
					users = draw_students(antal_elever_pr_tjans)
				
				ids = []
				for user in users:
					ids.append(user['student_id'])
				
				for initial in tagged_teachers:
					ids.append(teachers[initial])
				
				id_string = ",".join(str(n) for n in ids)

				#print(id_string)
				print("Headline - {} : {}".format(måltid, tjans))
				print("Description - {}".format('elevernes navne'))
				print("Startdate - {}".format(day))
				print("Starttime - {}".format(tidspunkt[0]))
				print("Enddate - {}".format(day))
				print("Endtime - {}".format(tidspunkt[1]))
				print("Users - {}".format(id_string))
				print("\n")

				headline = "{} : {}".format(måltid, tjans)
				description = "{}".format('Sæt en alarm, hvis du ikke kan huske det!')
				startdate = "{}".format(day)
				starttime = "{}".format(tidspunkt[0])
				enddate = "{}".format(day)
				endtime = "{}".format(tidspunkt[1])
				users = "{}".format(id_string)
				create_calendar_event(headline=headline, description=description, startdate=startdate, starttime=starttime, enddate=enddate, endtime=endtime, studentid=id_string)

				print("{} - {} - {} :::: {} -- {}".format(day, måltid, tjans, tidspunkt[0], tidspunkt[1]))

	print('ELEVER UDEN TJANS: {}'.format(len(weekend_students)))
	for elev in weekend_students:
		print(elev['name'])
	#create_calendar_event(startdate=date_string, starttime='18:00', enddate=date_string, endtime='20:30', userid=2756)
app()