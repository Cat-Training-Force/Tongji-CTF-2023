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
# flag{P2ng_1s_n0t_s@@@f3}