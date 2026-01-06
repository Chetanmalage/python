# Implementing real-time / technical applications using Exception Handling in Python.

# Design and implement a Python program that uses exception handling to manage
# errors in a real-world application.
# Your program should demonstrate:
#     1. Use of try, except, else, and finally blocks
#     2. Handling multiple exceptions
#     3. Custom exception creation
#     4. Real-time input validation
#     5. Graceful program termination without crashing


# Step 1: Create a Custom Exception
class InsufficientBalanceError(Exception):
    pass


# Step 2: Define the BankAccount Class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# Step 3: Implement Exception Handling (Real-Time Execution)
def bank_application():
    account = BankAccount("Chetan", 5000)

    while True:
        try:
            print("\n------ BANK MENU ------")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

            elif choice == 2:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

            elif choice == 3:
                account.display_balance()

            elif choice == 4:
                print("Thank you for using the bank system.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as ve:
            print("Input Error:", ve)

        except InsufficientBalanceError as ibe:
            print("Transaction Error:", ibe)

        except Exception as e:
            print("Unexpected Error:", e)

        else:
            print("Transaction completed successfully.")

        finally:
            print("System ready for next operation.")


# Step 4: Run the Application
bank_application()
