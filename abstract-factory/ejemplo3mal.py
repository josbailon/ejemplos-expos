from abc import ABC, abstractmethod
from factory_boy import Factory, SubFactory

# Definir la interfaz de la fábrica abstracta
class PizzaFactory(Factory):
    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_toppings(self):
        pass

# Fábrica concreta para pizzas de masa gruesa (incorrecta)
class ThickCrustPizzaFactory:
    def create_dough(self):
        return "Thick crust"

    def create_sauce(self):
        return "BBQ"

    def create_toppings(self):
        return ["Chicken", "Mushrooms"]

# Cliente
class PizzaStore:
    def create_pizza(self, factory):
        dough = factory.create_dough()
        sauce = factory.create_sauce()
        toppings = factory.create_toppings()
        return dough, sauce, toppings

# Crear una pizza utilizando una fábrica concreta (incorrecta)
thick_crust_factory = ThickCrustPizzaFactory()
pizza_store = PizzaStore()
pizza = pizza_store.create_pizza(thick_crust_factory)
print("Thick Crust Pizza (Incorrect):", pizza)
