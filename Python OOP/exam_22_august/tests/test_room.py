from unittest import TestCase, main

from project.people.child import Child
from project.rooms.room import Room



class TestRoom(TestCase):
    def setUp(self) -> None:
        self.room = Room("Name_test", 100, 1)


    def test_init_method(self):
        self.assertEqual("Name_test", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(1, self.room.members_count)
        self.assertEqual(0, self.room.expenses)
        self.assertEqual([], self.room.children)

    def test_expenses_set_to_positive(self):
        self.room.expenses = 30

        self.assertEqual(30, self.room.expenses)

    def test_expenses_set_to_zero(self):
        self.room.expenses = 0
        self.assertEqual(0, self.room.expenses)

    def test_expenses_set_to_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -10
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_calculate_expenses(self):
        child = [Child(5, 5, 5)]
        child_1 = [Child(5, 5, 6)]
        # room_1 = YoungCouple("Test_2", 500, 500)
        self.room.calculate_expenses(child, child_1)
        self.assertEqual(930, self.room.expenses)


if __name__ == "__main__":
    main()