import random
import hashlib
import time

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

# SEED = int(time.time())
SEED = 1682475336
random.seed(SEED)
KEY = random.randbytes(1024 // 8)
print(SEED)

if __name__ == "__main__":
    pngbytes = None
    with open('./flag.png', 'rb') as f:
        pngbytes = f.read()
    with open('flag.png.encrypted', 'wb') as f:
        f.write(encrypt(KEY, pngbytes))
