from bs4 import BeautifulSoup
import json
import requests
import asyncio
import os
from pyppeteer import launch
from u import user, pw

#Dette program skal få fat I elevernes tal og data.
# Deres viggo-id, elev-nummer, værelse og navn.

page2 = "";
mydivs = "";
student_list = [];
async def main():
    global cookies
    global page2
    global student_list
    global mydivs

    url = 'https://nordborgslot.viggo.dk/Basic/Users/List/30'

    page2 = requests.get(url, headers = {'cookie':'.AspNetCore.Session=CfDJ8DlDOVGwEK1NtQWCvIp6h529QqHbd01TBhq4p0QYW9ccstj5a%2FKfFOba1XQk2c5%2F%2FQshUyAXxDTx9QxyRLmDK2MvfZVKnY9u1189AxdmkyZ2XBmGfOUs9hAhZ5Hoeak3wNqTW9qIi%2FR8mOClBvruSwRPKL2QEK%2B1cQL5I2IY3acT'})
    #page2 = requests.get(url, headers = {'cookie':'.AspNetCore.Session={}'.format(cookies)})  
    print(page2.text)
    soup = BeautifulSoup(page2.text, 'html.parser')
    mydivs = soup.findAll("div", {"class": "hint"})
    for item in mydivs:
    	student = {}
        student['student_id'] = item.img['src'][51:55]
    	student['name'] = item.h3.text
    	student['student_number'] = item.select('div')[0].text[-3:]
    	#student['student_room'] = item.select('div')[1].text[-3:]
    	student_list.append(student)
    
    for person in student_list:
        print(person)
  
    with open('data.txt', 'w', encoding='utf8') as outfile:
        json.dump(student_list, outfile, ensure_ascii=False)
    
asyncio.get_event_loop().run_until_complete(main())