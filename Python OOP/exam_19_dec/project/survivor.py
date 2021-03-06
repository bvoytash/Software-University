class Survivor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.needs = 100

    @property
    def needs_sustenance(self):
        if self.needs < 100:
            return True
        return False

    @property
    def needs_healing(self):
        if self.health < 100:
            return True
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")
        self.__age = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def needs(self):
        return self._needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError("Needs not valid!")
        elif value > 100:
            self._needs = 100
        else:
            self._needs = value
