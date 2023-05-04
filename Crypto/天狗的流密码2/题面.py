from random import seed, randbytes
from secrets import token_hex

SEED = token_hex()
print(SEED)
seed(SEED)

def encrypt(b: bytes) -> bytes:
    assert len(b) % 4 == 0
    e = []
    for i in range(len(b) // 4):
        key = randbytes(4)
        for p, k in zip(b[i*4:i*4+4], key):
            e.append(p ^ k)
    return bytes(e)

test = open("./flag.png.encrypted", "rb").read()
test = test.ljust((len(test) // 4 + 1) * 4, b"\x00")
open("./flag.png.encrypted.encrypted", "wb").write(encrypt(test))

flag = open("./flag.png", "rb").read()
flag = flag.ljust((len(flag) // 4 + 1) * 4, b"\x00")
open("./flag.png.encrypted2", "wb").write(encrypt(flag))

