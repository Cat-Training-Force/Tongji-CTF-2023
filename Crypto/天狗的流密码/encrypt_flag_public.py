# Python 3.9.12 (main, Apr  5 2022, 01:53:17) 
# [Clang 12.0.0 ] :: Anaconda, Inc. on darwin
import random
import hashlib
import time

def calc_sha256(b):
    s = hashlib.sha256()
    s.update(b)
    return s.digest()

def getkeynbyte(key, n):
    ks = calc_sha256(key)
    i = n // len(ks)
    j = n % len(ks)
    for _ in range(i):
        ks = calc_sha256(ks)
    return ks[j]

def encrypt(key, data):
    ret = []
    for i, b in enumerate(data):
        ret.append(b ^ getkeynbyte(key, i))
    return bytes(ret)

SEED = int(time.time())
random.seed(SEED)
KEY = random.randbytes(1024 // 8)
print(SEED)

if __name__ == "__main__":
    pngbytes = None
    with open('./flag.png', 'rb') as f:
        pngbytes = f.read()
    with open('flag.png.encrypted', 'wb') as f:
        f.write(encrypt(KEY, pngbytes))
