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

# Fábrica concreta para pizzas de masa fina
class ThinCrustPizzaFactory(PizzaFactory):
    def create_dough(self):
        return "Thin crust"

    def create_sauce(self):
        return "Tomato"

    def create_toppings(self):
        return ["Cheese", "Pepperoni"]

# Cliente
class PizzaStore:
    def create_pizza(self, factory):
        dough = factory.create_dough()
        sauce = factory.create_sauce()
        toppings = factory.create_toppings()
        return dough, sauce, toppings

# Crear una pizza utilizando una fábrica concreta
thin_crust_factory = ThinCrustPizzaFactory()
pizza_store = PizzaStore()
pizza = pizza_store.create_pizza(thin_crust_factory)
print("Thin Crust Pizza:", pizza)
