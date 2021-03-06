from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name, price, grams, calories):
        super().__init__(name, self.__class__.PRICE, self.__class__.GRAMS, self.__class__.CALORIES)
