# 环境配置

1. 找一个双频路由器
2. 5G 广播 SSID 作为【表】的 flag，2.4G不广播 SSID 作为【里】的 flag
3. 找一台 Mac，使用 `whatchwificat.sh` 来保持对隐藏的 SSID 的连接
4. 拍摄具有 GPS 信息的照片，作为题目附件

tjctf{Ss1D_1s_1nt3reSt1n9}
tjctf{7hi5_I$_HIDd#N_Fla6}

【表】
writeup 要点：
1. 提到 metadata 中的 GPS 信息
2. 提到 GPS 的 offset （Optional）
3. 现场扫到 SSID

【里】
writeup 要点：
1. 使用 deauth 攻击获取到隐藏的 SSID
