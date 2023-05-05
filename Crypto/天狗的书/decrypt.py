dd = {'0': '5', '1': '0', '2': '2', '3': '6', '4': '3', '5': '9', '6': '8', '7': '4', '8': '7', '9': '1', 'A': 'G', 'B': 'B', 'C': 'M', 'D': 'N', 'E': 'E', 'F': 'D', 'G': 'Q', 'H': 'Y', 'I': 'R', 'J': 'C', 'K': 'A', 'L': 'S', 'M': 'U', 'N': 'W', 'O': 'V', 'P': 'I', 'Q': 'O', 'R': 'X', 'S': 'J', 'T': 'H', 'U': 'P', 'V': 'K', 'W': 'T', 'X': 'L', 'Y': 'F', 'Z': 'Z', '~': '{', '!': '.', '@': '*', '#': '#', '$': '<', '%': '&', '^': '^', '&': '>', '*': '$', '(': '(', ')': '_', '_': '+', '+': '?', '{': '%', '}': '}', '|': '"', ':': '!', '"': ')', ',': '~', '.': '|', '/': ':', '<': '@', '>': '/', '?': ','}

d = dict()
for k,v in dd.items():
    d[v] = k

kjv = None
with open('Book_encrypted.txt','r') as f:
    kjv = f.read()

n = len(kjv)
print(n)
with open('Book_decrypted.txt','w') as f:
    for i, ch in enumerate(kjv):
        if ch in d:
            f.write(d[ch])
        else:
            f.write(ch)
        if i % 100000 == 0:
            print(i // 100000, '/', n // 100000)

print("THE FLAG OF TJCTF{WORD_FREQUENCY_MAT7ER5}".lower())