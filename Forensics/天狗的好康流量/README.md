# 天狗的好康流量

**Difficulty:** medium

## 题目描述

*Challenge and description by MiaoTony and HH.*

这是什么，是好康的瑟图！！！

天狗在上班摸鱼的时候，不小心将自己刚生成的瑟图上传到了公司的服务器上，并且被公司的流量监管系统抓到了。

你要不要也来看看这是个什么图？


## 题目解析

解压拿到流量包，找到一个更新个人信息的接口

`POST /api/Employee/PostEmployeeInfo`

payload 里面的 avatar 是 base64 编码的图片

图片最后拼接了一个 zip 压缩包，解压需要密码

图片的 blue0 层隐写了一个二维码，扫码得到压缩包密码 `s0X231thL_kJpzO@`

解开压缩包得到 flag

`tjctf{do_U_1Ike_Ma7ryO$hka}`