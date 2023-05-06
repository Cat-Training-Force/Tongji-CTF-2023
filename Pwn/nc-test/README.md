# nc-test

**Difficulty:** Baby

## 题目描述

*Challenge and description by MiaoTony.*

这是一道送分题！

你能连接到服务器，获得这题的 flag 吗？

nc 是一个常用的网络工具，也称为 netcat。其主要用途是建立和监听任意 TCP 和 UDP 连接，支持 IPv4 和 IPv6，可以用来网络调试、端口扫描等等。

你可以上网查查 nc 的使用方法，这里随意丢一篇：[netcat 的使用](https://www.cnblogs.com/Lmg66/p/13811636.html)

假设给出的实例入口为 `host:port`，那么你可以使用 `nc host port` 来连接到对应的实例。

## 题目解析

**暴露端口：`1234`**

直接 nc 连接到服务器即可获取 flag。
