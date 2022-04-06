from project.animal import Animal
from project.tiger import Tiger
from project.lion import Lion
from project.cheetah import Cheetah
from project.worker import Worker
from project.keeper import Keeper
from project.vet import Vet
from project.caretaker import Caretaker

class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals) and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_need_to_pay = 0
        for w in self.workers:
            total_need_to_pay += w.salary
        if total_need_to_pay <= self.__budget:
            self.__budget -= total_need_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_need_money = 0
        for a in self.animals:
            total_need_money += a.money_for_care
        if self.__budget >= total_need_money:
            self.__budget -= total_need_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        message = []
        message.append(f"You have {len(self.animals)} animals")
        lions = []
        tigers = []
        cheetah = []
        for a in self.animals:
            if a.__class__.__name__ == "Lion":
                lions.append(a)
            elif a.__class__.__name__ == "Tiger":
                tigers.append(a)
            elif a.__class__.__name__ == "Cheetah":
                cheetah.append(a)
        message.append(f"----- {len(lions)} Lions:")
        for l in lions:
            message.append(repr(l))
        message.append(f"----- {len(tigers)} Tigers:")
        for t in tigers:
            message.append(repr(t))
        message.append(f"----- {len(cheetah)} Cheetahs:")
        for c in cheetah:
            message.append(repr(c))
        return "\n".join(message)

    def workers_status(self):
        message = []
        message.append(f"You have {len(self.workers)} workers")
        keepers = []
        caretakers = []
        vets = []
        for w in self.workers:
            if w.__class__.__name__ == "Keeper":
                keepers.append(w)
            elif w.__class__.__name__ == "Caretaker":
                caretakers.append(w)
            elif w.__class__.__name__ == "Vet":
                vets.append(w)
        message.append(f"----- {len(keepers)} Keepers:")
        for k in keepers:
            message.append(repr(k))
        message.append(f"----- {len(caretakers)} Caretakers:")
        for c in caretakers:
            message.append(repr(c))
        message.append(f"----- {len(vets)} Vets:")
        for v in vets:
            message.append(repr(v))
        return "\n".join(message)


# simba = Tiger("Simba", "male", 5)
# zoo = Zoo("zoo", 1000, 10, 10)
# print(zoo.add_animal(simba, 100))
# boro = Keeper("boro", 20, 150)
# print(zoo.hire_worker(boro))
# print(zoo.pay_workers())
# print(zoo.tend_animals())
# print(zoo.animals_status())






