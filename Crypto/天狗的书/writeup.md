# 天狗的书 Writeup

## 命题意图

考察古典密码的破解手段。

## 解法

### 预期解


1. 观察文本文件（熵和英文文档接近），发现字母表被打乱，按英语字母频率分析，可获得（大部分原文）。
2. 阅读部分解码的原文，可发现文本文件内容为英文经典作品 KJV Bible。
3. 根据章节编号还原数字的替换方式。
4. 全文搜索 TJCTF 得到 flag。

一些可以使用的工具：
```
https://github.com/healym3/SubstitutionBreaker
https://github.com/Ciphey/Ciphey
...
```

例如，使用 SubstitutionBreaker 对其中一段字符尝试破解：
```
Tongji-CTF-2023 % subbreaker break --lang EN --text "HYE VSN HEJHGUEWH VD HYE ARWQ CGUEJ KEXJRVW VD HYE BRBSE"
Alphabet: abcdefghijklmnopqrstuvwxyz
Key:      gboaedqyritsmwvcfujhxlkpnz
Fitness: 105.2
Nbr keys tried: 1449175
Keys per second: 149451
Execution time (seconds): 9.697
Plaintext:
THE OLY TESTARENT OF THE DING PARES WEUSION OF THE BIBLE
```


### 非预期解

一眼看出是 KJV Bible，找到原文后直接对照解答。