# test-final.py
import unittest
from unittest.mock import patch

class TestCalculators(unittest.TestCase):

    @patch('tkinter.Tk')  # Заменяем Tk на заглушку
    def test_personal_calculator(self, mock_tk):
        # Ваш тест для personal_calculator
        pass

    @patch('tkinter.Tk')  # Заменяем Tk на заглушку
    def test_mortgage_calculator(self, mock_tk):
        # Ваш тест для mortgage_calculator
        pass

    @patch('tkinter.Tk')  # Заменяем Tk на заглушку
    def test_basic_calculator(self, mock_tk):
        # Ваш тест для basic_calculator
        pass

if __name__ == '__main__':
    unittest.main()