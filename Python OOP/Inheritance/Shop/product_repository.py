from project.product import Product
from project.drink import Drink
from project.food import Food

class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name):
        for p in self.products:
            if p.name == product_name:
                self.products.remove(p)

    def __repr__(self):
        a = []
        for p in self.products:
            a.append(f"{p.name}: {p.quantity}")
        return "\n".join(a)


# apple = Food("apple")
# cola = Drink("cola")
# water = Drink("water")
# p_r = ProductRepository()
#
# p_r.add(cola)
# p_r.add(water)
# p_r.add(apple)
# print(p_r.__repr__())


