class Product:
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "Operation A"

class ConcreteProductB(Product):
    def operation(self):
        return "Operation B"

# Cliente
class Client:
    def use_products(self):
        product_a = ConcreteProductA()
        product_b = ConcreteProductB()
        print("Product A:", product_a.operation())
        print("Product B:", product_b.operation())

# Uso del patrón Abstract Factory de manera incorrecta
client = Client()
client.use_products()
