from randcrack import RandCrack

def decrypt(b: bytes) -> bytes:
    assert len(b) % 4 == 0
    e = []
    for i in range(len(b) // 4):
        key = rc.predict_getrandbits(32).to_bytes(4, "little")
        for p, k in zip(b[i*4:i*4+4], key):
            e.append(p ^ k)
    return bytes(e)

rc = RandCrack()
fpe = open("./flag.png.encrypted", "rb").read()
fpe = fpe.ljust((len(fpe) // 4 + 1) * 4, b"\x00")
fpee = open("./flag.png.encrypted.encrypted", "rb").read()
known_bytes = bytes([a ^ b for a, b in zip(fpe, fpee)])

for i in range(624):
    rc.submit(int.from_bytes(known_bytes[i*4:i*4+4], byteorder="little"))
for i in range(len(known_bytes) // 4 - 624):
    rc.predict_getrandbits(32)

fpe2 = open("./flag.png.encrypted2", "rb").read()
fp = decrypt(fpe2)
open("./flag.png.decrypted", "wb").write(fp)

