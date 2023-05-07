# 天狗破防的二维码


## 题目描述

*Challenge by MiaoTony, description by MiaoTony and ChatGPT.*

天狗与女神在无边无际的虚拟网络中漫步，听着微风拂过键盘的声音，又看着屏幕上的花花世界。突然，女神给天狗发来一个神秘的二维码。

天狗感到心跳加速，手指颤抖着，还没来得及仔细观察，突然软件崩溃了。他顿时惊恐万分，整个人破防了！

现在给你一个充当天狗女神的机会，发挥你的想象力让天狗破防吧！


## 题目解析

复刻一下四月底微信等应用扫神奇二维码会闪退的 bug（现在其实还有挺多 APP 还没修捏）

简单来说，APP 在扫描畸形二维码时，由于畸形二维码内的错误数据块导致 `libqbar.so` 崩溃，进而导致软件闪退。

构造畸形二维码样本时需要注意的要点：
- 数据块内不可以出现 Padding Pattern
- 最后一个 block 的内容为空，但是 Character Count Indicator 不为 0


另外，特地 ban 掉了网上常见的崩溃二维码，需要选手自己生成喵~

（由于目前已修复的 opencv-contrib 对应的 python 库还没 release，甚至还没有成功打包出来的 rolling 包，于是为了实现这个功能，喵喵专门自己编译了一份 opencv-python，还踩了一堆坑，太痛苦了

poc 详见 [exp.py](exp.py)，参考 NanoApe 的 [畸形二维码导致 APP 扫码模块崩溃](https://nano.ac/posts/86257129/)

*题外话：出这个问题的第二天凌晨看着群友 GZTime 在研究这个二维码崩溃的原理，一觉醒来发现 NanoApe 和 GZTime 已经发现源码的问题在发 PR 修复了，后来就想着拿来出成一道 CTF 题目好了喵~*
