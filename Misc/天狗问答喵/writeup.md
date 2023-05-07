# 天狗问答 Writeup

## 命题意图

考察信息检索能力，即 OSINT。

## 解法

- Q1
  - 在 Bing 中直接搜索「同济大学图书馆SciFinder数据库单一来源采购项目」
  - http://xxgk.tongji.edu.cn/index.php?classid=4584&newsid=15640&t=show
  - 答案：`109.6069`
- Q2
  - 在 Bing 中直接搜索「同济大学 IBM Mainframe」
  - 问 New Bing 或者 Bard
  - https://sse.tongji.edu.cn/kxyj/IBMzx.htm
  - 答案：`Z900`
- Q3
  - 在 Bing 中搜索 「TOSA2020寒假活动 内存杂谈」
  - 发现 「【TOSA2020寒假活动】#1 内存杂谈 by kernel.bin 加壹Plusone 」，顺着搜索，拿到宣讲视频
  - https://www.bilibili.com/video/BV1GV411b7M4
  - 快进看完视频，在 49 分钟左右，有一张内存的图片，清晰度只足够辨认内存的种类为 256MB DDR-400MHz-CL3
  - 截图后扔进 Google 等图片搜索，得到内存生产厂商为 ProMOS
  - Bing 搜索「ProMOS 256MB DDR-400MHz-CL3」，得到待选型号，与图像进行比对
  - 答案：`V826632K24SATG-D3`
- Q4
  - 在 GitHub 上直接搜索 `03acac914f039b1`，得到的 commit 即结果
  - 答案：`迟到的签到`
- Q5
  - 直接打开网址，发现 404，资源不存在
  - 看到提示中的「时光机」，使用 webarchive，可以直接下载原文件
  - 计算 md5 值即可
  - 答案：`2375191217b329cb8f518e706213636f`
- Q6
  - 在同济大学新闻网上搜索「同济大学第一届信息安全竞赛」
  - https://news.tongji.edu.cn/info/1003/41201.htm
  - 答案：`23`