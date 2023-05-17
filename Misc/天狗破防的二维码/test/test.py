import ctypes
# import faulthandler
# 在import之后直接添加以下启用代码即可
# faulthandler.enable()
import traceback


def test_segmentation_fault():
    # 对于segmentation fault并不能catch到异常，即此处try没效果
    try:
        ctypes.string_at(0)
    except Exception as e:
        print(traceback.format_exc())


if __name__ == "__main__":
    print(11111111)
    try:
        test_segmentation_fault()
    except:
        print(222222)
