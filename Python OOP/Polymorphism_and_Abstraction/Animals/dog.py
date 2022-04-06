from project.animal import Animal


class Dog(Animal):
    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    def make_sound(self):
        return "Woof!"


sharo = Dog("sharo", 8, "male")
print(repr(sharo))
print(sharo.make_sound())
