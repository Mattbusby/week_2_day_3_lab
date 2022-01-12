import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Basic Bar", 1000.00, ["Pint", "shot", "can"])

    def test_pub_has_name(self):
        self.assertEqual("Basic Bar", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(1000, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(["Pint", "shot", "can"], self.pub.drinks)

    # def test_increase_till(self):
    #     self.pub.increase_till(2.50)
    #     self.assertEqual(102.50, self.pub.till)
