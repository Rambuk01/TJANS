# read student json
import json
all_students_data = []
data = "";

def load_all_students():
	global all_students_data
	global data;
	data = open('elev_data_v2122.txt', encoding="utf8")
	all_students_data = json.load(data)
	print('Henter elev ID data.')



def load_weekend_students():
	global all_students_data
	weekend = open('weekend_student_data.txt', encoding="utf8")
	weekend_students = json.load(weekend)

	WEEKEND_STUDENTS_ID_LIST = [] # Elever der bliver på skolen, med deres ID
	try:
		for num, weekend_student in enumerate(weekend_students):
			print(weekend_student)
			student = next(item for item in all_students_data if int(item["student_number"]) == weekend_student['student_number'])
			WEEKEND_STUDENTS_ID_LIST.append({"name": student['name'], "student_id": student['student_id']})
			
	except Exception as e:
		print("ERROR : " + str(e))
		print('Probably couldnt find items... check student_data.py')	

	with open('weekend_student_data_id.txt', 'w') as outfile:
			json.dump(WEEKEND_STUDENTS_ID_LIST, outfile)
	print('Weekend elever ID liste gemt.')
	print('{} students loaded'.format(len(WEEKEND_STUDENTS_ID_LIST)))
"""
def load_weekend_students():
	global all_students_data
	weekend = open('weekend_student_data.txt', encoding="utf8")
	weekend_students = json.load(weekend)

	WEEKEND_STUDENTS_ID_LIST = [] # Elever der bliver på skolen, med deres ID
	try:
		for num, weekend_student in enumerate(weekend_students):
			student = next(item for item in all_students_data if item["student_number"] == weekend_student['student_number'])
			WEEKEND_STUDENTS_ID_LIST.append({"name": student['name'], "student_id": student['student_id']})
			print(weekend_student)
	except:
		print("ERROR : " + str(e))
		print('Probably couldnt find items... check student_data.py')

	with open('weekend_student_data_id.txt', 'w') as outfile:
			json.dump(WEEKEND_STUDENTS_ID_LIST, outfile)
	print('Weekend elever ID liste gemt.')
	#print('{} students loaded'.format(len(WEEKEND_STUDENTS_ID_LIST)))
"""