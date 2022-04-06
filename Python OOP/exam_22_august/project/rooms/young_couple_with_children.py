from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room
from project.people.child import Child


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_two+salary_one, len(children) + 2)

        self.room_cost = 30
        self.children = list(children)
        self.appliances = []
        for _ in range(len(children) + 2):
            self.appliances.append(Laptop())
            self.appliances.append((TV()))
            self.appliances.append(Fridge())
        self.expenses = 30 * sum([obj.cost for obj in self.appliances]) \
                        + sum([obj.cost for obj in self.children]) * 30
