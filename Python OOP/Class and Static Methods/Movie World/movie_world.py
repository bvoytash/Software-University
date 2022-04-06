from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    _DVD_CAPACITY = 15
    _CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        # capacity = 15
        # current_capacity = capacity - len(self.dvds)
        return MovieWorld._DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        # capacity = 10
        # current_capacity = capacity - len(self.customers)
        return MovieWorld._CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if MovieWorld._CUSTOMER_CAPACITY > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if MovieWorld._DVD_CAPACITY > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer_name = [c.name for c in self.customers if c.id == customer_id][0]
        customer_object = [c for c in self.customers if c.id == customer_id][0]
        dvd_name = [d.name for d in self.dvds if d.id == dvd_id][0]
        dvd_object = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd_object.is_rented and dvd_object in customer_object.rented_dvds:
            return f"{customer_name} has already rented {dvd_name}"
        elif dvd_object.is_rented:
            return "DVD is already rented"
        elif customer_object.age < dvd_object.age_restriction:
            return f"{customer_name} should be at least {dvd_object.age_restriction} to rent this movie"

        customer_object.rented_dvds.append(dvd_object)
        dvd_object.is_rented = True
        return f"{customer_name} has successfully rented {dvd_name}"

    def return_dvd(self, customer_id, dvd_id):
        customer_name = [c.name for c in self.customers if c.id == customer_id][0]
        customer_object = [c for c in self.customers if c.id == customer_id][0]
        dvd_name = [d.name for d in self.dvds if d.id == dvd_id][0]
        dvd_object = [d for d in self.dvds if d.id == dvd_id][0]
        if dvd_object in customer_object.rented_dvds:
            customer_object.rented_dvds.remove(dvd_object)
            dvd_object.is_rented = False
            return f"{customer_name} has successfully returned {dvd_name}"
        return f"{customer_name} does not have that DVD"

    def __repr__(self):
        result = []
        for i in self.customers:
            result.append(repr(i))
        for j in self.dvds:
            result.append(repr(j))
        return '\n'.join(result)


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))
print(movie_world.dvd_capacity())
# print(repr(movie_world))
