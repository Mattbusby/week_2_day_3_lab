import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Fernando", 20, 27)
    
    def test_customer_has_name(self):
        self.assertEqual("Fernando", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual( 20 , self.customer.wallet)

    def test_pay_for_drink(self):
        self.customer.pay_for_drink(5)
        self.assertEqual(15, self.customer.wallet)