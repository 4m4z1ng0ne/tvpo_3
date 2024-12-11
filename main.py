import tkinter as tk
from calculator import PersonalCalculator

def personal_calculator():
    def add_transaction():
        amount = float(amount_entry.get())
        description = description_entry.get()
        is_income = income_var.get()
        new_balance = calculator.add_transaction(amount, description, is_income)
        balance.set(new_balance)
        transactions_list.insert(tk.END, f"{'+' if is_income else '-'}{amount:.2f} - {description}")
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)

    calculator = PersonalCalculator()
    window = tk.Tk()
    window.title("Калькулятор личных средств")
    window.configure(bg="#f0f0f0")

    balance = tk.DoubleVar(value=0.0)
    balance_label = tk.Label(window, textvariable=balance, bg="#f0f0f0", font=("Arial", 14))
    balance_label.pack(pady=10)

    amount_label = tk.Label(window, text="Сумма:", bg="#f0f0f0")
    amount_label.pack()
    amount_entry = tk.Entry(window, bg="#ffffff", borderwidth=2)
    amount_entry.pack()

    income_var = tk.BooleanVar(value=True)
    income_radio = tk.Radiobutton(window, text="Доход", variable=income_var, value=True, bg="#f0f0f0")
    income_radio.pack()
    expense_radio = tk.Radiobutton(window, text="Расход", variable=income_var, value=False, bg="#f0f0f0")
    expense_radio.pack()

    description_label = tk.Label(window, text="Описание:", bg="#f0f0f0")
    description_label.pack()
    description_entry = tk.Entry(window, bg="#ffffff", borderwidth=2)
    description_entry.pack()

    add_button = tk.Button(window, text="Добавить", command=add_transaction, bg="#4CAF50", fg="white", borderwidth=2)
    add_button.pack(pady=10)

    transactions_label = tk.Label(window, text="Транзакции:", bg="#f0f0f0")
    transactions_label.pack()
    transactions_list = tk.Listbox(window, bg="#ffffff")
    transactions_list.pack()

    window.mainloop()

if __name__ == '__main__':
    personal_calculator()