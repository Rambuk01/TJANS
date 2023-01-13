# draw_function.py

from load_weekend_list import load_weekend_students
import random

weekend_students = load_weekend_students()

def draw_students(number_to_draw=3):
	global weekend_students
	drawn = []
	# draw 3 random dicts from weekend_students list.
	for number in range(number_to_draw):
		rnd = int(random.randrange(0, len(weekend_students)))
		student = weekend_students.pop(rnd)
		drawn.append(student)

	return drawn


#Hvis under 93 elever. Træk 3
# Hvis over 93 elever. Træk 4

if __name__ == '__main__':
	print('ELEVER UDEN TJANS: ')
	for elev in weekend_students:
		print(elev['name'])
