from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("Test", 100)

    def test_init_method(self):
        self.factory = PaintFactory("Test", 100)
        self.assertEqual("Test", self.factory.name)
        self.assertEqual(100, self.factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_add_product_which_not_exist(self):
        self.factory.add_ingredient("white", 20)
        self.assertEqual(20, self.factory.ingredients['white'])

    def test_add_product_which_exist(self):
        self.factory.add_ingredient("white", 20)
        self.assertEqual(20, self.factory.ingredients['white'])
        self.factory.add_ingredient("white", 20)
        self.assertEqual(40, self.factory.ingredients['white'])

    def test_add_product_which_is_not_valid(self):
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient("dark", 20)
        self.assertEqual(f"Ingredient of type dark not allowed in PaintFactory", str(ex.exception))

    def test_add_product_not_enough_capacity(self):
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient('white', 200)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_remove_quantity_from_product(self):
        self.factory.add_ingredient("white", 20)
        self.factory.remove_ingredient("white", 20)
        self.assertEqual(0, self.factory.ingredients["white"])

    def test_remove_more_quantity_than_exist(self):
        self.factory.add_ingredient("white", 20)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient("white", 30)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_product_not_in_ingredients(self):
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient('test_2', 20)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_property_ingredient(self):
        self.factory.add_ingredient("white", 20)
        self.assertEqual({"white": 20}, self.factory.products)


if __name__ == "__main__":
    main()