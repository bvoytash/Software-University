from exam_10_april.aquarium.freshwater_aquarium import FreshwaterAquarium
from exam_10_april.aquarium.saltwater_aquarium import SaltwaterAquarium
from exam_10_april.decoration.decoration_repository import DecorationRepository
from exam_10_april.decoration.ornament import Ornament
from exam_10_april.decoration.plant import Plant
from exam_10_april.fish.freshwater_fish import FreshwaterFish
from exam_10_april.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            new_aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(new_aquarium)
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            new_aquarium = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(new_aquarium)
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            new_decoration = Ornament()
            self.decorations_repository.decorations.append(new_decoration)
            return f"Successfully added {decoration_type}."
        elif decoration_type == "Plant":
            new_decoration = Plant()
            self.decorations_repository.decorations.append(new_decoration)
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = [el for el in self.aquariums if el.name == aquarium_name]
        decoration_list = [el for el in self.decorations_repository.decorations if el.__class__.__name__ == decoration_type]
        if aquarium and decoration_list:
            aquarium[0].decorations.apppend(decoration_list[0])
            self.decorations_repository.decorations.remove(decoration_list[0])
            return f"Successfully added {decoration_type} to {aquarium_name}."
        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):

        new_fish = None
        aquarium = [el for el in self.aquariums if el.name == aquarium_name][0]

        if fish_type == "FreshwaterFish":
            new_fish = FreshwaterFish(fish_name, fish_species, price)
            if aquarium.__class__.__name__ == "SaltwaterAquarium":
                return "Water not suitable."

        elif fish_type == "SaltwaterFish":
            new_fish = SaltwaterFish(fish_name, fish_species, price)
            if aquarium.__class__.__name__ == "FreshwaterAquarium":
                return "Water not suitable."

        if not new_fish:
            return f"There isn't a fish of type {fish_type}."
        aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = [el for el in self.aquariums if el.name == aquarium_name][0]
        aquarium.feed()
        return f"Fish fed: {len(aquarium[0].fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [el for el in self.aquariums if el.name == aquarium_name][0]
        fish_price = sum([obj.price for obj in aquarium.fish])
        decoration_price = sum([obj.price for obj in aquarium.decorations])
        total_sum = fish_price + decoration_price
        return f"The value of Aquarium {aquarium_name} is {total_sum:.2f}."

    def report(self):
        pass









