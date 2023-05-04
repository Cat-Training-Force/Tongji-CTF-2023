flag = b"tjctf{...}"
from Crypto.Util.number import *

def mul_mod(x, y, p):
    return (x + y + x * y) % p

def pow_mod(x, num, p):
    result = 0
    while num != 0:
        if num % 2 == 1:
            result = mul_mod(x, result, p)
        x = mul_mod(x, x, p)
        num //= 2
    return result

# 生成公私钥
p = getPrime(300)
x = getRandomNBitInteger(128)
# n = {secret number}
y = pow_mod(x, n, p)

# 加密
m = bytes_to_long(flag)
r = getRandomNBitInteger(128)
rx = pow_mod(x, r, p)
rym = pow_mod(y, r, p) + m

# 输出
print(f"""
p = {p}
x = {x}
y = {y}
rx = {rx}
rym = {rym}
""")
p = 1922897127076788767906402618734870007752452012165091530909481875757051779767613064581018973
x = 182422121544511674376185201210214257549
y = 1835992202367133706193954120819184820969901760569440616725865323933265822891912083770421197
rx = 1322684511875890043434976068915861919081202332753527529243156148305646768295405692383427845
rym = 1553712184220848973952059769995611076069705030698301578919829072455723124880317278036718344

