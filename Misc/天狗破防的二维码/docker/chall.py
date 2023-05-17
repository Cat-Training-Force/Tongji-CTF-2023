import cv2
import sys
import base64
import numpy as np
import os
import subprocess

FLAG = os.getenv("GZCTF_FLAG")
if FLAG == "":
    FLAG = "tjctf{QRc0d3_1S_5O_fuN_TESTFLAG}"

demo_str_list = ['KFCVW50         ',
                 '\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01',
                 '1145141.1145141.1145141.1145141']

is_crash = False
print("Welcome to Tiangou's QRcode!\n")
img_base64 = input("Please input your QRcode in base64-encoded format: \n")
try:
    img_bytes = base64.b64decode(img_base64)
    with open('input.png', 'wb') as f:
        f.write(img_bytes)
    img_buffer_numpy = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(img_buffer_numpy, cv2.IMREAD_COLOR)
except:
    print("---------------------------------------------------------------")
    print("Input ERROR!")
    sys.exit(0)

print("---------------------------------------------------------------")

try:
    # WeChat detector
    detector = cv2.wechat_qrcode_WeChatQRCode("", "", "", "")
except:
    print("---------------------------------------------------------------")
    print("Failed to initialize WeChatQRCode. Please report to admin!")
    sys.exit(0)

try:
    # Official detector
    QRmodel = cv2.QRCodeDetector()
    codeinfo, pts, outs = QRmodel.detectAndDecode(img)
    if pts is None:
        print("No QRcode!")
        sys.exit(0)
    print(codeinfo, pts)
except Exception as e:
    print("---------------------------------------------------------------")
    print(e)
    print("What's your input???")
    sys.exit(0)

try:
    res, points = detector.detectAndDecode(img)
    print("---------------------------------------------------------------")
    print(res, points)
    res_ = ''.join(res) if res else ''
    for demo in demo_str_list:
        if demo in res_:
            print("---------------------------------------------------------------")
            print("Oh, you should generate it by yourself!\nTry again!")
            sys.exit(0)
except Exception as e:
    # except cv2.error as e:
    # Only valid on Windows...
    # print(e)
    # if "Unknown C++ exception" in str(e):
    #     is_crash = True
    print("Decode ERROR!")
    sys.exit(0)

# pip install opencv-contrib-python-headless==4.7.0.72
args = ["/home/ctf/env1/bin/python", "-c",
        "import cv2;img = cv2.imread('input.png');detector = cv2.wechat_qrcode_WeChatQRCode('', '', '', '');res, points = detector.detectAndDecode(img);print(res)"]
process = subprocess.Popen(
    args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
try:
    stdout, stderr = process.communicate(timeout=8)
except subprocess.TimeoutExpired:
    process.kill()
    stdout, stderr = process.communicate()
print("---------------------------------------------------------------")
print(stdout.decode())
print(stderr.decode())
if process.returncode != 0:
    is_crash = True


print("---------------------------------------------------------------")
if is_crash:
    print("Great! It did crash!\nThis is your flag:")
    print(FLAG)
else:
    print("Come on!")
