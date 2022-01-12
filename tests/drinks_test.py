import unittest
from src.drinks import Drinks

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks("Blue Nun", 5)
    
    
    def test_drink_has_name(self):
        self.assertEqual("Blue Nun", self.drinks.name)