# Ret2libc 

> VOiD | Thursday 27 January 2022 02:59:45 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.250.107


## Return oriented programming (ROP)
```

    The basis of return-oriented programming is chaining together small chunks of code already present within the binary itself in such a way as to do what we wish. For example, reading flag.txt file, or even better, getting a shell.
```

## ret2libc attack
```

    The ret2libc is ROP with a small difference. The difference is that these small chunks of code which we'll be using are in the dynamically linked c library called libc.
    Why do we use libc? Well, it's already linked to our binary, and libc has some of the functions which are interesting to us. One of the functions which are useful to us is called "system" which lets us execute anything passed to it.
    Now, what if I tell you that in libc, there is also a string value that looks like this: "/bin/sh". I think you now know where this is going.
    All we have to do is create an ROP chain (small chunks of code chained together) that passes the "/bin/sh" string as the argument to the system function and then call this function.
```

```bash
Username: andy
Password: ret2libc!
ssh andy@10.10.250.107
```

## Checksec
```bash
checksec exploit_me 
[*] '/home/void/tryhackme/Ret2libc/exploit_me'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)

```

## Offset
```bash
cyclic -l aafa                                                               1 ⨯
18
```



