class ValidateMeta(type):
    def __init__(cls, name, bases, namespace):
        # Base sınıfı atlayarak sadece alt sınıfları kontrol edelim
        if name != 'Base':
            required = getattr(cls, 'REQUIRED_FIELDS', ())
            for field in required:
                if not hasattr(cls, field):
                    raise TypeError(f"{name} must define {field}")
        super().__init__(name, bases, namespace)


class Base(metaclass=ValidateMeta):
    REQUIRED_FIELDS = ()


class User(Base):
    REQUIRED_FIELDS = ('id', 'name')
    id = 1
    name = "Alice"

# Aşağıdaki tanım TypeError atar:
# class BadUser(Base):
#     REQUIRED_FIELDS = ('id', 'name')
#     id = 2   # name eksik -> hata
