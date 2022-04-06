class Customer:
    id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        Customer.id += 1
        self.id = Customer.id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        # Customer.id += 1
        return Customer.id + 1


# c = Customer("boro", "sofia", "asd@mail")
# print(repr(c))
# d = Customer("boro", "plovdiv", "asd@mail")
# print(repr(d))
# print(c.get_next_id())

