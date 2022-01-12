import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Fernando", 20, 27)
        self.drink1 = Drinks("Lager", 5)
        self.drink2 = Drinks("Shot", 6)
        self.drinklist = [self.drink1, self.drink2]
        self.pub = Pub("Basic Bar", 1000.00, self.drinklist)

    def test_pub_has_name(self):
        self.assertEqual("Basic Bar", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(1000, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(2, len(self.pub.drinks))

    def test_increase_till(self):
        self.pub.increase_till(5)
        self.assertEqual(1005, self.pub.till)

    def test_check_age(self):
        result = self.customer.check_age(20)
        self.assertEqual(True, result)