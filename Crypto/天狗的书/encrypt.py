import random

chars = ''.join([chr(ord('A') + i) for i in range(26)])
symbols = r'~!@#$%^&*()_+{}|:",./<>?'
numbers = ''.join([chr(ord('0') + i) for i in range(10)])

c = list(numbers+chars+symbols)
sn = list(numbers)
sc = list(chars)
ss = list(symbols)

random.shuffle(sn)
random.shuffle(sc)
random.shuffle(ss)
d = dict(zip(c,sn+sc+ss))

print(d)

kjv = None
with open('KJV.txt','r') as f:
    kjv = f.read()
kjv = kjv.upper()

n = len(kjv)
print(n)
with open('Book_encrypted.txt','w') as f:
    for i, ch in enumerate(kjv):
        if ch in d:
            f.write(d[ch])
        else:
            f.write(ch)
        if i % 100000 == 0:
            print(i // 100000, '/', n // 100000)
