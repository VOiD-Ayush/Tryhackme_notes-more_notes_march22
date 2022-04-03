# Magician 

> VOiD | Thursday 11 November 2021 10:25:17 PM IST

My IP : 10.8.253.221
Target IP : 10.10.247.64

## PORT 21
```bash
ftp 10.10.127.33
Connected to 10.10.127.33.
220 THE MAGIC DOOR
Name (10.10.127.33:void): anonymous
331 Please specify the password.
Password:
230-Huh? The door just opens after some time? You're quite the patient one, aren't ya, it's a thing called 'delay_successful_login' in /etc/vsftpd.conf ;) Since you're a rookie, this might help you to get started: https://imagetragick.com. You might need to do some little tweaks though...
230 Login successful.

```

## PORT 8080 [http]


## PORT 8081 [http]

upload the exploit.png


## USER [Magician]

```bash
magician@magician:~$ cat user.txt 
THM{simsalabim_hex_hex}

magician@magician:~$ cat the_magic_continues 
The magician is known to keep a locally listening cat up his sleeve, it is said to be an oracle who will tell you secrets if you are good enough to understand its meows.

magician@magician:~$ netstat -l
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 localhost:6666          0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:tproxy          0.0.0.0:*               LISTEN     


curl -X POST localhost:6666 -d "filename=/etc/passwd"
curl -X POST localhost:6666 -d "filename=/root/root.txt"


GUZ{zntvp_znl_znxr_znal_zra_znq}

--> ROT13
```

