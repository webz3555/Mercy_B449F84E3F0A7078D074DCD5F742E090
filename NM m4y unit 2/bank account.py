class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of the BankAccount class
    account1 = BankAccount("123456789", "John Doe", 1000)

    # Deposit money
    account1.deposit(500)

    # Withdraw money
    account1.withdraw(200)

    # Display the account balance
    account1.display_balance()
