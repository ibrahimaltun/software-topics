class SimpleFramework:
    """
    plugin callback - Hollywood Principle
    """

    def __init__(self):
        self._plugins = []

    def register_plugin(self, plugin):
        # plugin: herhangi bir objenin on_event metodunu bekliyoruz
        self._plugins.append(plugin)

    def run(self, data):
        # Framework kontrol ediyor; pluginleri çağırıyor -> "Don't call us, we'll call you"
        for p in self._plugins:
            # plugin kendi davranışını burada gerçekleştirir
            p.on_event(data)


class MyPlugin:
    """
        Kullanıcı tarafından sağlanan plugin
    """

    def on_event(self, data):
        print("Plugin received:", data)


if __name__ == "__main__":
    fw = SimpleFramework()
    fw.register_plugin(MyPlugin())
    fw.run({"msg": "Hello IoC / Hollywood!"})
