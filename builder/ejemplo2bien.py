from dataclasses import dataclass

# Clase producto
@dataclass
class Pizza:
    dough: str
    sauce: str
    toppings: list

# Clase Builder
class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza("", "", [])

    def set_dough(self, dough):
        self._pizza.dough = dough
        return self

    def set_sauce(self, sauce):
        self._pizza.sauce = sauce
        return self

    def add_topping(self, topping):
        self._pizza.toppings.append(topping)
        return self

    def build(self):
        return self._pizza

# Creación de una pizza utilizando el builder
pizza_builder = PizzaBuilder()
pizza = pizza_builder.set_dough("Thin crust").set_sauce("Tomato").add_topping("Cheese").add_topping("Pepperoni").build()
print(pizza)
