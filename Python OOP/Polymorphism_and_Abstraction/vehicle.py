from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self,distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    air_conditioners_per_liter = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        need_liters = distance * (self.fuel_consumption + Car.air_conditioners_per_liter)
        if need_liters <= self.fuel_quantity:
            self.fuel_quantity -= need_liters
            return self.fuel_quantity
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):
    air_conditioners_per_liter = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        need_liters = distance * (self.fuel_consumption + Truck.air_conditioners_per_liter)
        if need_liters <= self.fuel_quantity:
            self.fuel_quantity -= need_liters
            return self.fuel_quantity
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel
        return self.fuel_quantity


