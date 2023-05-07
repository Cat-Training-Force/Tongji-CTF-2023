# 天狗的流密码 Writeup

## 命题意图

考察流密码的破解，伪随机数生成器和 Crib 的相关概念，同时考察代码审计能力。

## 解法

1. 理解加密使用的代码的原理
2. 意识到伪随机数的关键性
3. 意识到 png 文件头的前几个字节是固定的
4. 使用 png 的文件头几个字节对伪随机数种子进行爆破
5. 解密时顺便优化一下加密使用的代码，是其变为线性复杂度

### 预期解

```python
import random
import hashlib
import time

seed = int(time.time())

png_header = [137, 80, 78, 71, 13, 10, 26, 10]

encrypted_pngbytes = None
with open('./flag.png.encrypted', 'rb') as f:
    encrypted_pngbytes = f.read()
print(len(encrypted_pngbytes))
print(list(encrypted_pngbytes[:8]))

key_header = [png_header[i] ^ encrypted_pngbytes[i] for i in range(8)]
print(key_header)
key_header = bytes(key_header)

# UTC+8 2023-01-01 00:00:00 -> 1672502400
while seed > 1672502400:
    random.seed(seed)
    tkey = random.randbytes(1024 // 8)
    sha = hashlib.sha256()
    sha.update(tkey)
    if sha.digest()[:8] == key_header:
        print(seed)
        break
    seed -= 1

def calc_sha256(b):
    s = hashlib.sha256()
    s.update(b)
    return s.digest()

def encrypt(key, data):
    ret = []
    ks = calc_sha256(key)
    for i, b in enumerate(data):
        if i >= len(ks):
            ks += calc_sha256(ks[len(ks)-32:])
        ret.append(b ^ ks[i])
        if i % 1000 == 0:
            print(i // 1000, '/', (len(data) // 1000))
    return bytes(ret)

random.seed(seed)
KEY = random.randbytes(1024 // 8)
with open('flag.png.encrypted', 'rb') as f:
    with open('flag_recovered.png', 'wb') as ff:
        ff.write(encrypt(KEY, f.read()))

# 得到图片扫码得到flag
```

