# load_weekend_list.py
import json

def load_weekend_students():
	data = open('weekend_student_data_id.txt', encoding="utf8")
	return json.load(data)

if __name__ == '__main__':
	data = load_weekend_students()
	print(data)