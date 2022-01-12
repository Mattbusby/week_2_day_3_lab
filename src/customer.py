class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def pay_for_drink(self, price):
        self.wallet -= price

    def check_age(self, age):
        if age >= 18:
            return True
        else:
            return False
