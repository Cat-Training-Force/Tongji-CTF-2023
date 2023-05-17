import qrcode
from qrcode.util import *

def hack_put(self, num, length):
    if num == 0:
        num = 233 # make a fake length
    for i in range(length):
        self.put_bit(((num >> (length - i - 1)) & 1) == 1)

qrcode.util.BitBuffer.put = hack_put

qr = qrcode.QRCode(2, qrcode.constants.ERROR_CORRECT_M, mask_pattern=0)

num_data = QRData('1145141', MODE_NUMBER)
data = QRData(b'.', MODE_8BIT_BYTE)
hack_data = QRData(b'', MODE_8BIT_BYTE)

# make sure all data is fit to the max content length for this version
qr.add_data(num_data)
qr.add_data(data)
qr.add_data(num_data)
qr.add_data(data)
qr.add_data(num_data)
qr.add_data(data)
qr.add_data(num_data)
# add a zero length data to make the length of the data to be 233
qr.add_data(hack_data)

qr.make_image().save("demo3.png")
