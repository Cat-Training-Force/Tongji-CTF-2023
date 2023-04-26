import re
import random
with open('in.py') as f:
    s = f.read()

values = re.findall(r'lambda (.*?):', s)
values = set(v.strip() for value in values for v in value.split(','))
used = set()
for v in values:
    while True:
        nv = ''.join(random.choice('oоοօ') for _ in range(5))
        if not nv in used:
            used.add(nv)
            break
    s = s.replace(v, nv)

with open('out.py', 'w', encoding='utf-8') as f:
    f.write(s)