from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        result = sum([obj.comfort for obj in self.decorations])
        return result

    def add_fish(self, fish):
        current_capacity = self.capacity - sum([obj.capacity for obj in self.fish])
        if self.capacity < current_capacity + fish.capacity:
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def str(self):
        result = [f"{self.name}:"]
        if self.fish:
            result.append(f"Fish: {' '.join([fish.name for fish in self.fish])}")
        else:
            result.append(f"Fish: none")
        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {sum([el.comfort for el in self.decorations])}")






