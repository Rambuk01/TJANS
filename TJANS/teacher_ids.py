# teacher_ids.py

teachers = {
'ak': 2754,
'bn': 124,
'bj': 142,
'gb': 1531,
'hv': 3668,
'jc': 128,
'jl': 681,
'jb': 129,
'kj': 2755,
'kp': 4103,
'lj': 131,
'ln': 133,
'lh': 4102,
'mbl': 3602,
'mf': 2756,
'mm': 1693,
'ma': 134,
'rm': 137,
'sb': 3670,
'sj': 2758,
}
running = True
tagged_teachers = []
while running:
	tag_input = str(input('Hvem skal Tagges? (f.eks. mf). "Q" for stop\n'))
	
	if tag_input == "q":
		running = False;
	else:
		if tag_input in teachers:
			tagged_teachers.append(tag_input)
		else:
			print('Ingen med initialerne: {}'.format(tagged_teachers))

"""
for initial in tag:
	teacher_id_list.append(teachers[initial])
ids = []
for initial in teacher_id_list:
	ids.append(teachers[initial])
"""
#teacher_id_string = ",".join(teacher_id_list)