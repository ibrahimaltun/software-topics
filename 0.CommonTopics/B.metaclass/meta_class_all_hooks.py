
"""
Mini-ORM demo showing metaclass hooks:
- __prepare__: keep attribute definition order
- __new__: collect Field descriptors into _fields, add __repr__
- __init__: register model classes and validate primary key existence
- __call__: identity-map (one instance per PK) with thread-safety
"""

from collections import OrderedDict
import threading
from typing import Any, Dict, OrderedDict as OrderedDictType


class Field:
    """Simple Field descriptor for model attributes"""

    def __init__(self, *, primary_key: bool = False, default: Any = None):
        self.primary_key = primary_key
        self.default = default
        self.name = None  # will be set by metaclass

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self  # access via class => descriptor itself
        return instance.__dict__.get(self.name, self.default)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class ModelMeta(type):
    """Metaclass implementing the hooks"""
    # global registry of model classes
    registry: Dict[str, "ModelMeta"] = {}
    # lock used for thread-safe identity-map creation
    _global_lock = threading.Lock()

    # 1) __prepare__: use OrderedDict so field order is preserved
    @classmethod
    def __prepare__(mcls, name, bases):
        return OrderedDict()

    # 2) __new__: collect Field instances and build metadata
    def __new__(mcls, name, bases, namespace):
        # collect Field objects preserving definition order
        fields: "OrderedDictType[str, Field]" = OrderedDict()
        for key, value in list(namespace.items()):
            if isinstance(value, Field):
                value.name = key
                fields[key] = value
        namespace["_fields"] = fields  # attach metadata to the class object
        # determine primary key name if any
        pk_name = None
        for fname, fobj in fields.items():
            if fobj.primary_key:
                pk_name = fname
                break
        namespace["_pk_name"] = pk_name

        # add a helpful __repr__ if not provided
        if "__repr__" not in namespace:
            def __repr__(self):
                clsname = self.__class__.__name__
                parts = ", ".join(
                    f"{k}={getattr(self, k)!r}" for k in self._fields.keys())
                return f"<{clsname} {parts}>"
            namespace["__repr__"] = __repr__

        cls = super().__new__(mcls, name, bases, dict(namespace))
        print(
            f"[ModelMeta.__new__] Created class {name}, fields={list(fields.keys())}, pk={pk_name}")
        return cls

    # 3) __init__: register model class and validate it
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        # avoid registering the base Model itself
        if name != "Model":
            ModelMeta.registry[name] = cls
            # validate presence of primary key
            if cls._pk_name is None:
                raise TypeError(
                    f"Model '{name}' must declare one Field(primary_key=True)")
            # prepare per-class identity map and lock
            cls._identity_map: Dict[Any, "Model"] = {}
            cls._identity_lock = threading.Lock()
            print(
                f"[ModelMeta.__init__] Registered Model '{name}' with pk='{cls._pk_name}'")

    # 4) __call__: implement identity map (one instance per PK), thread-safe
    def __call__(cls, *args, **kwargs):
        # We expect pk to be provided as kwarg (e.g., User(id=1, ...))
        pk_name = cls._pk_name
        if pk_name is None:
            # should not happen because __init__ validated it, but be defensive
            return super().__call__(*args, **kwargs)

        pk_value = kwargs.get(pk_name)
        if pk_value is None:
            # If no PK provided, create a transient (non-cached) instance
            return super().__call__(*args, **kwargs)

        # identity map lookup/create, thread-safe
        with cls._identity_lock:
            if pk_value in cls._identity_map:
                # return existing instance (do NOT call __init__ again)
                print(
                    f"[ModelMeta.__call__] Returning cached instance for {cls.__name__}({pk_name}={pk_value!r})")
                return cls._identity_map[pk_value]
            else:
                # create a new instance and cache it
                instance = super().__call__(*args, **kwargs)
                cls._identity_map[pk_value] = instance
                print(
                    f"[ModelMeta.__call__] Created and cached instance for {cls.__name__}({pk_name}={pk_value!r})")
                return instance


class Model(metaclass=ModelMeta):
    """Base Model using the metaclass"""

    def __init__(self, **kwargs):
        # set all declared fields from kwargs or default
        for fname, fobj in self._fields.items():
            if fname in kwargs:
                setattr(self, fname, kwargs[fname])
            elif fobj.default is not None:
                setattr(self, fname, fobj.default)
        # simple persisted flag to mimic ORM behaviour
        self._persisted = False

    def save(self):
        # mock save: mark as persisted
        pk = getattr(self, self._pk_name)
        if pk is None:
            raise ValueError("Primary key must be set before saving")
        self._persisted = True
        print(
            f"[Model.save] Persisted {self.__class__.__name__}({self._pk_name}={pk!r})")


# --- Example model definitions and demo usage ---
if __name__ == "__main__":
    # Define a model: User
    class User(Model):
        id = Field(primary_key=True)
        name = Field(default="anonymous")
        email = Field(default=None)

    # Define another model: Product
    class Product(Model):
        sku = Field(primary_key=True)
        title = Field()
        price = Field(default=0.0)

    print("\n--- Registry content ---")
    print(ModelMeta.registry)

    print("\n--- Field order preserved ---")
    print("User._fields order:", list(User._fields.keys()))
    print("Product._fields order:", list(Product._fields.keys()))

    print("\n--- Creating instances (identity map demo) ---")
    u1 = User(id=1, name="Alice", email="alice@example.com")
    u2 = User(id=1)  # should return same object as u1 (cached)
    print("u1 is u2:", u1 is u2)
    print("u1:", u1)
    print("u2:", u2)

    print("\n--- Transient instance when no PK provided ---")
    t1 = User(name="Transient")
    t2 = User(name="Transient")
    print("t1 is t2 (transient):", t1 is t2)

    print("\n--- Thread-safety test: concurrent creation of same PK ---")
    created = []

    def make_user(pk, idx):
        inst = User(id=pk, name=f"Thread-{idx}")
        created.append((idx, id(inst), inst.name))

    threads = [threading.Thread(target=make_user, args=(42, i))
               for i in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Created instances info (idx, object_id, name):")
    for info in created:
        print(info)
    # verify all object ids are the same
    unique_obj_ids = set(info[1] for info in created)
    print("Unique object ids count (should be 1):", len(unique_obj_ids))

    print("\n--- Show saving and persisted flag ---")
    u1.save()
    print("u1._persisted:", u1._persisted)
