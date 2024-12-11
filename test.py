import unittest
from calculator import PersonalCalculator

class TestPersonalCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = PersonalCalculator()

    def test_add_income(self):
        new_balance = self.calculator.add_transaction(100.00, "Зарплата", True)
        self.assertEqual(new_balance, 100.00)
        self.assertEqual(self.calculator.get_balance(), 100.00)

    def test_add_expense(self):
        self.calculator.add_transaction(100.00, "Зарплата", True)
        new_balance = self.calculator.add_transaction(50.00, "Покупка", False)
        self.assertEqual(new_balance, 50.00)
        self.assertEqual(self.calculator.get_balance(), 50.00)

    def test_negative_balance(self):
        self.calculator.add_transaction(50.00, "Зарплата", True)
        new_balance = self.calculator.add_transaction(100.00, "Расход", False)
        self.assertEqual(new_balance, -50.00)
        self.assertEqual(self.calculator.get_balance(), -50.00)

if __name__ == '__main__':
    unittest.main()