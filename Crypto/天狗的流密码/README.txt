文件夹内容：
.
├── README.txt               说明文件
├── encrypt_flag_fast.py     用于出题人生成 flag.png.encrypted 的脚本
├── encrypt_flag_public.py   公开的加密脚本
├── flag.png                 有 flag 二维码的原图片
├── flag.png.encrypted       加密后的文件
├── flag_qr.png              flag 图片中的二维码
├── flag_recovered.png       解密后的图片
├── solution.py              解题脚本
├── 题面.md


出题时只要附上 猫猫的流密码.zip 即可

扫描解密后的图像中的二维码即可拿到flag
tjctf{P2ng_1s_n0t_s@@@f3}
当时的 seed=1682475336

writeup 要点：
1. 提到 png 文件头
2. 提到 SEED = int(time.time()) 和 random.seed(SEED) 可以爆破
