from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room
from project.people.child import Child


class YoungCouple(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one+salary_two, 2)
        self.room_cost = 20
        self.appliances = []
        for i in range(0, 2):
            self.appliances.append(Laptop())
            self.appliances.append((TV()))
            self.appliances.append(Fridge())
        self.expenses = sum([obj.cost for obj in self.appliances])  * 30