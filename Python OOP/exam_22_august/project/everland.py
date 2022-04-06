from project.rooms.room import Room


class Everland():
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_expenses = 0
        for obj in self.rooms:
            total_expenses += obj.room_cost
            total_expenses += obj.expenses * 30
        return f"Monthly consumption: {total_expenses:.2f}$."

    def pay(self):
        result = []

        for obj in self.rooms:
            family_budget = obj.budget
            total_expenses = 0
            total_expenses += obj.room_cost
            total_expenses += obj.expenses

            if family_budget >= total_expenses:
                new_budget = family_budget - total_expenses
                obj.budget = new_budget
                result.append(f"{obj.family_name} paid {total_expenses:.2f}$ and have {new_budget:.2f}$ left.")

            else:
                result.append(f"{obj.family_namename} does not have enough budget and must leave the hotel.")
                self.rooms.remove(obj)
        return '\n'.join(result)


    def status(self):
        pass