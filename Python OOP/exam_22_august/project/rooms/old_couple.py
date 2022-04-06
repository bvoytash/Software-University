from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room
from project.people.child import Child


class OldCouple(Room):

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one+pension_two, 2)
        self.room_cost = 15
        self.appliances = []
        for i in range(0, 2):
            self.appliances.append(Stove())
            self.appliances.append((TV()))
            self.appliances.append(Fridge())
        self.expenses = sum([obj.cost for obj in self.appliances]) * 30
