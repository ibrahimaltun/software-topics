"""
pizza_builder_step.py

Step-Builder örneği: adımların belirli sırada yapılmasını sağlar.
Kullanım:
    b = StepPizzaBuilder.start().with_size("Medium").with_crust("Thick").add_topping("Olives").build()
"""
from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Pizza:
    size: str
    crust: str
    toppings: List[str] = field(default_factory=list)
    extra_cheese: bool = False


# Araçsallık: her adım farklı bir sınıf döndürüyor
class _AfterSizeBuilder:
    def __init__(self, size: str):
        self._size = size

    def with_crust(self, crust: str):
        return _AfterCrustBuilder(self._size, crust)


class _AfterCrustBuilder:
    def __init__(self, size: str, crust: str):
        self._size = size
        self._crust = crust
        self._toppings: List[str] = []
        self._extra_cheese = False

    def add_topping(self, topping: str):
        self._toppings.append(topping)
        return self  # yine crust sonrası eklemeye devam edilebilir

    def extra_cheese(self, enable: bool = True):
        self._extra_cheese = enable
        return self

    def build(self) -> Pizza:
        # all required parts present by design (size & crust)
        return Pizza(
            size=self._size,
            crust=self._crust,
            toppings=list(self._toppings),
            extra_cheese=self._extra_cheese
        )


class StepPizzaBuilder:
    """Entry point: start() ile başlanır ve zincir adımları çağrılır."""
    @staticmethod
    def start():
        """Başlangıç: only with_size() is allowed next"""
        class _Starter:
            def with_size(self, size: str):
                return _AfterSizeBuilder(size)
        return _Starter()


# Demo
if __name__ == "__main__":
    # Geçerli kullanım (sıra zorunlu): önce size, sonra crust, sonra toppings ve build
    pizza = (StepPizzaBuilder
             .start()
             .with_size("Medium")
             .with_crust("Stuffed")
             .add_topping("Tomato")
             .add_topping("Basil")
             .extra_cheese()
             .build())
    print("Step pizza:", pizza)

    # Yanlış kullanım: with_crust çağrılmadan add_topping mümkün değil (API sunmuyor)
    try:
        # StepPizzaBuilder.start().with_crust("Thin")  # hata: _Starter nesnesinin with_crust metodu yok
        pass
    except Exception as e:
        print("Beklenen hata (örnek):", e)
