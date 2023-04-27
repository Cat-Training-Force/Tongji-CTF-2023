# 天狗的加密消息

## 题面

天狗最近喜欢上了一款游戏，但他在队内交流的时候遇到了问题：有些文字发不出去！但他转念一想，自己两年前获得了[Python 学位考核](https://github.com/Cat-Training-Force/Tongji-CTF-2021/tree/master/Reverse/PyMaster)的证书，而游戏队内交流可以发图片文件……所以他想出了一个小花招！

## 附件

`make rebuild` 以后，把 `build` 文件夹下的 `tougue_dog` 文件夹打包分发。

## 题解

直接执行 `pyc` 什么都没给，尝试 load 一下？

```python
# 假设我是 3.11，pyc 文件自行改名
from importlib.util import module_from_spec, spec_from_file_location
path = 'tougue_dog/tougue_dog.cpython-311.pyc'
spec = spec_from_file_location('tougue_dog.cpython-311', path)
op = module_from_spec(spec)
spec.loader.exec_module(op)
print(op.__dir__())
print(op.Foo().__dir__())
print(op.Bar().__dir__())
print(op.Bar.decrypt_flag(op.Foo.get_flag()))
```

```python
# nemo @ nemo-workstation in D:\UserData\Documents\Projects\py-playground [15:03:32]
$ py .\test.py
['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'abc', 'b64decode', 'mapping_rp', 'mapping_en', 'rp_to_en', 'en_to_rp', 'AnyAbstractClass', 'Foo', 'Bar']
['__module__', 'some_method', 'get_flag', '__doc__', '__abstractmethods__', '_abc_impl', 'any_validation_method', 'decrypt_flag', '__dict__', '__weakref__', '__slots__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
['__module__', 'some_method', 'decrypt_flag', '__doc__', '__abstractmethods__', '_abc_impl', 'any_validation_method', 'get_flag', '__dict__', '__weakref__', '__slots__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
tjctf{remember_no_russian}
```