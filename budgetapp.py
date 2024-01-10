class Budget:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.expenses = {}

    def add_income(self, amount):
        self.balance += amount
        print(f"Income of ${amount} added. New balance: ${self.balance}")

    def add_expense(self, category, amount):
        if category not in self.expenses:
            self.expenses[category] = 0

        if amount > self.balance:
            print("Error: Insufficient funds.")
        else:
            self.balance -= amount
            self.expenses[category] += amount
            print(f"Expense of ${amount} in '{category}' category added. New balance: ${self.balance}")

    def get_summary(self):
        print("\nBudget Summary:")
        print(f"Current Balance: ${self.balance}")
        print("Expenses:")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")
        print("\n")

# Example usage:
budget = Budget(initial_balance=1000)

budget.add_income(2000)
budget.add_expense("Groceries", 150)
budget.add_expense("Utilities", 100)

budget.get_summary()
