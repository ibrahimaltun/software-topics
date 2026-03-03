"""
pizza_builder_fluent.py

Fluent Pizza Builder örneği:
- Zincirlenebilir API: size, crust, add_topping, extra_cheese, takeaway
- build() -> immutable Pizza dataclass
- Kullanım demo gösterir
"""
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class Pizza:
    size: str
    crust: str
    toppings: List[str] = field(default_factory=list)
    extra_cheese: bool = False
    takeaway: bool = False

    def description(self) -> str:
        t = ", ".join(self.toppings) if self.toppings else "no toppings"
        cheese = "with extra cheese" if self.extra_cheese else "no extra cheese"
        take = "takeaway" if self.takeaway else "dine-in"
        return f"{self.size} pizza ({self.crust}) - {t} - {cheese} - {take}"


class PizzaBuilder:
    """Fluent builder: adımlar serbest; build() çağrılmadan Pizza yaratılmaz."""

    def __init__(self):
        self._size: Optional[str] = None
        self._crust: Optional[str] = None
        self._toppings: List[str] = []
        self._extra_cheese: bool = False
        self._takeaway: bool = False

    def size(self, size: str) -> "PizzaBuilder":
        self._size = size
        return self

    def crust(self, crust: str) -> "PizzaBuilder":
        self._crust = crust
        return self

    def add_topping(self, topping: str) -> "PizzaBuilder":
        self._toppings.append(topping)
        return self

    def extra_cheese(self, flag: bool = True) -> "PizzaBuilder":
        self._extra_cheese = flag
        return self

    def takeaway(self, flag: bool = True) -> "PizzaBuilder":
        self._takeaway = flag
        return self

    def build(self) -> Pizza:
        # validation: gerekli alanlar
        if self._size is None:
            raise ValueError("Pizza size must be specified")
        if self._crust is None:
            # sağlayabilirsiniz: default değer atayabilirsiniz; burada zorunlu yapıyoruz
            raise ValueError("Pizza crust must be specified")
        # dönen Pizza immutable (frozen dataclass)
        return Pizza(
            size=self._size,
            crust=self._crust,
            toppings=list(self._toppings),
            extra_cheese=self._extra_cheese,
            takeaway=self._takeaway,
        )


# Demo
if __name__ == "__main__":
    # Fluent kullanım: esnek, okunaklı
    pizza = (PizzaBuilder()
             .size("Large")
             .crust("Thin")
             .add_topping("Mushrooms")
             .add_topping("Pepperoni")
             .extra_cheese(True)
             .takeaway(True)
             .build())
    print(pizza.description())

    # Hatalı kullanım örneği: build() çağrılmadan önce gerekli alanlar atlanırsa ValueError
    try:
        bad = PizzaBuilder().size("Small").build()
    except ValueError as e:
        print("Expected Error:", e)
