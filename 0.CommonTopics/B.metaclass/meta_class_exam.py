""" 
A simple metaclass example: it logs while creating class
"""


class ClassCreationLogger(type):
    """
    This class print out the class name and its attributes when instantiates a new class.
    """
    def __new__(mcls, name, bases, namespace):
        print(
            f"[ClassCreationLogger] Creating class {name} with attrs: {list(namespace.keys())}")
        return super().__new__(mcls, name, bases, namespace)


# Usage


class My(metaclass=ClassCreationLogger):
    x = 10
    def foo(self): pass

    def __new__(cls):
        print("new", cls)


class Sub(My):
    y = 20


if __name__ == "__main__":
    m = My()
    s = Sub()
