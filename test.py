import pytest
import tkinter as tk
from unittest.mock import patch

# Импортируем функции из вашего файла main.py
from main import personal_calculator, mortgage_calculator, basic_calculator

@pytest.fixture
def setup_tkinter():
    root = tk.Tk()
    yield root
    root.destroy()

def test_personal_calculator_opens(setup_tkinter):
    with patch('tkinter.Toplevel') as mock_toplevel:
        personal_calculator()
        mock_toplevel.assert_called_once()

def test_mortgage_calculator_opens(setup_tkinter):
    with patch('tkinter.Toplevel') as mock_toplevel:
        mortgage_calculator()
        mock_toplevel.assert_called_once()

def test_basic_calculator_opens(setup_tkinter):
    with patch('tkinter.Toplevel') as mock_toplevel:
        basic_calculator()
        mock_toplevel.assert_called_once()