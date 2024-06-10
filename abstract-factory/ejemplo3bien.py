from abc import ABC, abstractmethod

# Interfaz de la fábrica abstracta
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

# Fábrica concreta 1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

# Fábrica concreta 2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

# Interfaz de productos
class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass

# Producto concreto A1
class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "Operation A1"

# Producto concreto A2
class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "Operation A2"

# Interfaz de productos
class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass

# Producto concreto B1
class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "Operation B1"

# Producto concreto B2
class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "Operation B2"

# Cliente
class Client:
    def __init__(self, factory):
        self.factory = factory

    def use_products(self):
        product_a = self.factory.create_product_a()
        product_b = self.factory.create_product_b()
        print("Product A:", product_a.operation_a())
        print("Product B:", product_b.operation_b())

# Uso del patrón Abstract Factory
factory1 = ConcreteFactory1()
client1 = Client(factory1)
client1.use_products()

factory2 = ConcreteFactory2()
client2 = Client(factory2)
client2.use_products()
