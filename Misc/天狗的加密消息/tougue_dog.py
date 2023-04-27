import abc
from base64 import b64decode

mapping_rp = r'''́
щ
е
р
т
ы
у
и
о
п
а
с
д
ф
г
х
й
к
л
з
х
ц
в
б
н
м
Q
Щ
Е
Р
Т
Ы
У
И
О
П
А
С
Д
Ф
Г
Х
Й
К
Л
З
Х
Ц
В
Б
Н
М
+
/
='''.replace('\n', '')
mapping_en = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM+/='

rp_to_en = str.maketrans(mapping_rp, mapping_en)
en_to_rp = str.maketrans(mapping_en, mapping_rp)

# initial_flag = r'''т
# й
# ц
# т
# ф
# {
# р
# е
# м
# е
# м
# б
# е
# р
# _
# н
# о
# _
# р
# у
# с
# с
# и
# а
# н
# }'''.replace('\n', '')

# flag = b64encode(initial_flag.encode('utf-16-be')).decode('utf-8')
# print(flag)
# rp_flag = flag.translate(en_to_rp)
# print(rp_flag)

class AnyAbstractClass(abc.ABC):
    @abc.abstractmethod
    def some_method(self):
        ...

    def any_validation_method(self) -> bool:
        return
    
    @staticmethod
    def get_flag() -> str:
        raise NotImplementedError
    
    @staticmethod
    def decrypt_flag(flag: str) -> str:
        raise NotImplementedError

class Foo(AnyAbstractClass):

    def some_method(self):
        pass

    @staticmethod
    def get_flag() -> str:
        return 'БЕИЕОQРГБЕИЕРАБ7БЕАЕНQQ8БДУЕПАQхБДУЕQАБфБД0ЕПгБфБЕАЕQщРББЕЕЕОАQщБД0АфQ=='
    
class Bar(AnyAbstractClass):

    def some_method(self):
        pass

    @staticmethod
    def decrypt_flag(flag: str) -> str:
        return b64decode(flag.translate(rp_to_en).encode('utf-8')).decode('utf-16-be').translate(rp_to_en)
    
if __name__ == '__main__':
    print('🌙')