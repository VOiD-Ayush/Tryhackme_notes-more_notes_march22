# Reversing ELF

## Crackme 1

```bash

./crackme1 
flag{not_that_kind_of_elf}

```

## Crackme 2

```bash
strings crackem2
super_secret_password

./crackme2 super_secret_password
Access granted.
flag{if_i_submit_this_flag_then_i_will_get_points}

```

## Crackme 3
```bash
echo ZjByX3kwdXJfNWVjMG5kX2xlNTVvbl91bmJhc2U2NF80bGxfN2gzXzdoMW5nNQ | base64 -d
f0r_y0ur_5ec0nd_le55on_unbase64_4ll_7h3_7h1ng5
```

## Crackme 4
```bash
gdb crackme4
infofunctions
break @ strcmp
info registers
x/s at rdi

my_m0r3_secur3_pwd
```

## Crackme 5
```bash
python3 ape.py

OfdlDSA|3tXb32~X3tX@sX`4tXtz
```

## Crackme 6
```bash
Read crackme6.c
it tells 1337_pwd
```


## Crackme 7
```bash
./crackme7                                                                   1 ⨯
Menu:

[1] Say hello
[2] Add numbers
[3] Quit

[>] 31337
Wow such h4x0r!
flag{much_reversing_very_ida_wow}

```

## Crackme 8
```bash
in main
>>> -0x35010ff3
-889262067


./crackme8 -889262067                                                        1 ⨯

Access granted.
flag{at_least_this_cafe_wont_leak_your_credit_card_numbers}

```