enc = int.to_bytes(0x0EAA29EC6E8C5D9D30614222A4B514F6C, 16, 'little') \
    + int.to_bytes(0x0F4EBDEFD2825190F0B756074785DB89E, 16, 'little') \
    + int.to_bytes(0xEC998C89, 8, 'little') + b'\x91'

dec = []
xor = 24
for i in range(37):
    dec.append(enc[i] ^ xor)
    xor = (xor + 13) & 0xff

print(''.join(map(chr, dec)))
