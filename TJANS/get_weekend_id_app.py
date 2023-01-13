# get_weekend_id_app.py

"""
This program opens an xl file, exports the students that will stay.
Then it will load all students data (elev_data_v3).
It will combine the student that will stay, and retrieve their names and IDs and
store it in weekend_student_data_id.txt
"""

from get_weekend_names import *
from student_data import *
root = Tk()

openFile()
exportWeekendList()
load_all_students()
load_weekend_students()

root.withdraw()
root.destroy()


#Jeg laver kun root variablen, for at lukke et dumt vindue.