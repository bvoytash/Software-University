from project_1.user import User

class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user: User):
        for u in self.user_records:
            if u.name == user.username:
                self.user_records.append(user)
        return f"User with id = {user.id} already registered in the library!"

    def remove_user(self, user: User):
        for u in self.user_records:
            if u.name == user.username:
                self.user_records.remove(user)
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        for u in self.user_records:
            if u.username == new_username:
                return "Please check again the provided username - " \
                       "it should be different than the username used so far!"

        if user.username == new_username and user.user_id == user_id:
            return f"Username successfully changed to: {new_username} for userid: {user_id.id}"
        return f"There is no user with id = {user_id}!"




