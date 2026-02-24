class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # İlk kez oluşturma; super().__call__ __new__ ve __init__ çağrısını yapar
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            # Önceden oluşturulmuş instance döndürülüyor; __init__ tekrar çalışmaz
            pass
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    def __init__(self, value):
        print("Config.__init__ çalıştı, value =", value)
        self.value = value


if __name__ == "__main__":
    a = Config(1)  # __init__ çalışır
    b = Config(2)  # __init__ çalışmaz, aynı instance döner
    c = Config(3)  # __init__ çalışmaz, aynı instance döner

    print(a is b, id(a), id(b))
    print(a is c, id(a), id(c))
    print(b is c, id(b), id(c))

    print(a.value)
    print(b.value)
    print(c.value)
