from collections import OrderedDict


class OrderedMeta(type):
    @classmethod
    def __prepare__(mcls, name, bases):
        # Class bloğunda tanımlama sırasını korumak için OrderedDict döndürüyoruz
        return OrderedDict()

    def __new__(mcls, name, bases, namespace):
        # namespace artık OrderedDict olduğu için sıralamayı görebiliriz
        print(f"-{name}- sınıfı için definition sırası: {list(namespace.keys())}")
        return super().__new__(mcls, name, bases, dict(namespace))


class MySubClass(metaclass=OrderedMeta):
    a = 1
    def foo(self): pass
    b = 2


if __name__ == "__main__":
    pass
