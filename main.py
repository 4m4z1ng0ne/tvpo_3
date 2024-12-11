import tkinter as tk
from tkinter import messagebox

def personal_calculator():
    def add_transaction():
        amount = float(amount_entry.get())
        description = description_entry.get()
        if income_var.get():
            balance.set(balance.get() + amount)
            transactions_list.insert(tk.END, f"+{amount:.2f} - {description}")
        else:
            balance.set(balance.get() - amount)
            transactions_list.insert(tk.END, f"-{amount:.2f} - {description}")
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)

    window = tk.Toplevel(root)
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

def mortgage_calculator():
    def calculate_payment():
        loan_amount = float(loan_amount_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 1200
        loan_term = int(loan_term_entry.get()) * 12
        monthly_payment = (loan_amount * interest_rate) / (1 - (1 + interest_rate)**(-loan_term))
        payment_label.config(text=f"Ежемесячный платеж: {monthly_payment:.2f}")

    window = tk.Toplevel(root)
    window.title("Калькулятор ипотеки")
    window.configure(bg="#f0f0f0")
    
    loan_amount_label = tk.Label(window, text="Сумма кредита:", bg="#f0f0f0")
    loan_amount_label.pack(pady=5)
    loan_amount_entry = tk.Entry(window, bg="#ffffff", borderwidth=2)
    loan_amount_entry.pack(pady=5)

    interest_rate_label = tk.Label(window, text="Процентная ставка (%):", bg="#f0f0f0")
    interest_rate_label.pack(pady=5)
    interest_rate_entry = tk.Entry(window, bg="#ffffff", borderwidth=2)
    interest_rate_entry.pack(pady=5)

    loan_term_label = tk.Label(window, text="Срок кредита (лет):", bg="#f0f0f0")
    loan_term_label.pack(pady=5)
    loan_term_entry = tk.Entry(window, bg="#ffffff", borderwidth=2)
    loan_term_entry.pack(pady=5)

    calculate_button = tk.Button(window, text="Рассчитать", command=calculate_payment, bg="#4CAF50", fg="white", borderwidth=2)
    calculate_button.pack(pady=10)

    payment_label = tk.Label(window, text="", bg="#f0f0f0")
    payment_label.pack(pady=5)


def basic_calculator():
    def calculate():
        try:
            expression = entry.get()
            # Заменяем "%" на "/100" перед вычислением
            expression = expression.replace("%", "/100")
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except (SyntaxError, NameError, ZeroDivisionError):
            messagebox.showerror("Ошибка", "Неверное выражение.")

    def clear_last():
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text[:-1])

    def clear_all():
        entry.delete(0, tk.END)

    calculator_window = tk.Toplevel(root)
    calculator_window.title("Обычный калькулятор")
    calculator_window.configure(bg="#f0f0f0")  # Set background color

    entry = tk.Entry(calculator_window, width=30, bg="#ffffff", borderwidth=5)
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        '%',
    ]
    row_val = 1
    col_val = 0

    for button in buttons:
        button_text = button
        if button == '=':
            button_text = " = "
        tk.Button(calculator_window, text=button_text, width=7, command=lambda b=button: entry.insert(tk.END, b) if b != '=' else calculate(), bg="#e0e0e0", borderwidth=2).grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    # Кнопки удаления и процент
    tk.Button(calculator_window, text="C", width=7, command=clear_last, bg="#e0e0e0", borderwidth=2).grid(row=5, column=0, padx=5, pady=5)
    tk.Button(calculator_window, text="AC", width=7, command=clear_all, bg="#e0e0e0", borderwidth=2).grid(row=5, column=1, padx=5, pady=5)
    tk.Button(calculator_window, text="%", width=7, command=lambda: entry.insert(tk.END, '%'), bg="#e0e0e0", borderwidth=2).grid(row=5, column=2, padx=5, pady=5)


root = tk.Tk()
root.title("Выбор калькулятора")
root.configure(bg="#f0f0f0")


personal_finance_button = tk.Button(root, text="Калькулятор личных финансов", command=personal_calculator)
personal_finance_button.pack(pady=10)

mortgage_button = tk.Button(root, text="Ипотечный калькулятор", command=mortgage_calculator)
mortgage_button.pack(pady=10)


basic_calculator_button = tk.Button(root, text="Обычный калькулятор", command=basic_calculator)
basic_calculator_button.pack(pady=10)

root.mainloop()