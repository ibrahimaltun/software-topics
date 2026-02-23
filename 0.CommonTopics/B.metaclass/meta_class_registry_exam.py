class RegistryMeta(type):
    """keeps subclass registry"""
    registry = {}

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        # save also subclass not just baseclass
        if name != 'BasePlugin':
            RegistryMeta.registry[name] = cls


class BasePlugin(metaclass=RegistryMeta):
    pass


class PluginA(BasePlugin):
    pass


class PluginB(BasePlugin):
    pass


if __name__ == "__main__":
    print("Registered plugins:", RegistryMeta.registry)

    # usage example
    plugin_cls = RegistryMeta.registry.get("PluginA")
    inst = plugin_cls()
    print(type(inst))
