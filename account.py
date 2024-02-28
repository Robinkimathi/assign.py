class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Amount ${amount} deposited. Your current balance is ${self.balance}."
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Amount ${amount} withdrawn. Your current balance is ${self.balance}."
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive value."
        else:
            return "Insufficient funds. Your current balance is ${self.balance}."

    def check_balance(self):
        return f"Your current balance is ${self.balance}."

    def customer_details(self):
        return f"""Customer Name: {self.customer_name}
Account Number: {self.account_number}
Date of Opening: {self.date_of_opening}
Balance: ${self.balance}"""
