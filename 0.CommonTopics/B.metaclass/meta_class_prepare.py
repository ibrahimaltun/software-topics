from collections import OrderedDict


class OrderedMeta(type):
    @classmethod
    def __prepare__(mcls, name, bases):
        # Class bloğunda tanımlama sırasını korumak için OrderedDict döndürüyoruz
        return OrderedDict()

    def __new__(mcls, name, bases, namespace):
        # namespace artık OrderedDict olduğu için sıralamayı görebiliriz
        print(f"Definisyon sırası for {name}: {list(namespace.keys())}")
        return super().__new__(mcls, name, bases, dict(namespace))


class My(metaclass=OrderedMeta):
    a = 1
    def foo(self): pass
    b = 2


if __name__ == "__main__":
    # Program başında çıktı: Definisyon sırası for My: ['__module__','a','foo','b','__doc__']
    pass
