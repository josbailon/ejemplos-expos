# Clase producto
class Pizza:
    def __init__(self, dough, sauce, toppings):
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

# Creación directa de una pizza
pizza = Pizza("Thin crust", "Tomato", ["Cheese", "Pepperoni"])
print(pizza)
