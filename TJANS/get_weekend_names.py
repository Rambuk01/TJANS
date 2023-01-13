# get_weekend_names.py
from openpyxl import load_workbook
import json
import sys
from tkinter import *
from tkinter.filedialog import askopenfilename   

fname = "unassigned"
WEEKEND_DELTAGER_LIST = []
def openFile():
    global fname
    
    fname = askopenfilename()
    wb = load_workbook(filename=fname)
    sheet_ranges = wb['ViGGO']
    for row in sheet_ranges.rows:
        weekend_deltager = {}
    	
        if row[4].value == "Jeg er på NSE":
            weekend_deltager['name'] = "{} {}".format(row[0].value, row[1].value)
            try:
                weekend_deltager['student_number'] = int(row[3].value)
            except:
                print('Error getting student number in get_weekend_names.py')
                weekend_deltager['student_number'] = 606
            WEEKEND_DELTAGER_LIST.append(weekend_deltager)

                
    print("{} elever er på NSE i denne weekend!".format(len(WEEKEND_DELTAGER_LIST)))    

def exportWeekendList(*args):
	with open('weekend_student_data.txt', 'w', encoding='utf8') as outfile:
		json.dump(WEEKEND_DELTAGER_LIST, outfile, ensure_ascii=False)
	print('Weekend deltager liste gemt på PC.')

def quit(*args):
	root.destroy()

if __name__ == '__main__':

    root = Tk()
    Button(root, text='File Open', command = openFile).pack(fill=X)
    Button(root, text='Save data', command = exportWeekendList).pack(fill=X)
    Button(root, text='Quit', command = quit).pack(fill=X)

    mainloop()
