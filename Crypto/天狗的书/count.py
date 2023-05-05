chars = ''.join([chr(ord('A') + i) for i in range(26)])

d = dict(zip(list(chars), [0 for _ in range(len(chars))]))

s = None
with open('Book_encrypted.txt','r') as f:
    s = f.read()

n = 0
for ch in s:
    if ch in d:
        d[ch] += 1
        n += 1

res = [(v / n * 100, k) for k, v in d.items()]
res.sort(key=lambda x:-x[0])

freq = '''e 12.702%
t 9.056%
a 8.167%
o 7.507%
i 6.966%
n 6.749%
s 6.327%
h 6.094%
r 5.987%
d 4.253%
l 4.025%
c 2.782%
u 2.758%
m 2.406%
w 2.361%
f 2.228%
g 2.015%
y 1.974%
p 1.929%
b 1.492%
v 0.978%
k 0.772%
j 0.153%
x 0.150%
q 0.095%
z 0.074%'''.split('\n')
freq_l = []
for line in freq:
    l = line.strip().replace('%','').split(' ')
    freq_l.append((l[0].upper(), eval(l[1])))

for i in range(len(res)):
    if i < len(freq_l):
        print(res[i], freq_l[i])
    else:
        print(res[i])

decd = dict()

for i in range(26):
    decd[res[i][1]] = freq_l[i][0]

with open('Book_trydecrypt.txt','w') as f:
    for ch in s:
        if ch in decd:
            f.write(decd[ch])
        else:
            f.write(ch)
print("tjctf{WORDFREQUENCYMAT7ER5}".lower())