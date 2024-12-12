class PersonalCalculator:
    def __init__(self):
        self.balance = 0.0

    def add_transaction(self, amount, description, is_income):
        amount = float(amount)
        if is_income:
            self.balance += amount
        else:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance