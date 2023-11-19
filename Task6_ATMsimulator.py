class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited successfully. Your new balance is ${self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive number."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"${amount} withdrawn successfully. Your new balance is ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds. Your balance is not enough for this withdrawal."
        else:
            return "Invalid withdrawal amount. Please enter a positive number."

def main():
    atm = ATM()

    while True:
        print("\nATM Simulation")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print(atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter the deposit amount: "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Exiting the ATM simulation. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
