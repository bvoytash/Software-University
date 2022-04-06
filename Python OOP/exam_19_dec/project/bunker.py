from project.supply.water_supply import WaterSupply
from project.supply.food_supply import FoodSupply


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        result = [el for el in self.supplies if el.__class__.__name__ == "FoodSupply"]
        if result:
            return result
        raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        result = [el for el in self.supplies if el.__class__.__name__ == "WaterSupply"]
        if result:
            return result
        raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        result = [el for el in self.medicine if el.__class__.__name__ == "Painkiller"]
        if result:
            return result
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        result = [el for el in self.medicine if el.__class__.__name__ == "Salve"]
        if result:
            return result
        raise IndexError("There are no salves left!")

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        med_obj_list = [el for el in self.medicine if el.__class__.__name__ == medicine_type]
        med_obj = None
        if med_obj_list:
            med_obj = med_obj_list[-1]

        # if survivor.needs_healing:
            self.medicine.remove(med_obj)
            med_obj.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        sus_obj_list = [el for el in self.supplies if el.__class__.__name__ == sustenance_type]
        sus_obj = None
        if sus_obj_list:
            sus_obj = sus_obj_list[-1]

        # if survivor.needs_sustenance:
            self.supplies.remove(sus_obj)
            sus_obj.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
        for s in self.survivors:
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")


