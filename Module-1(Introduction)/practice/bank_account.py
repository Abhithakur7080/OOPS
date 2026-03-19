"""
BankAccount Class Demo (Object-Oriented Programming)

This script demonstrates a simple OOP example in Python.

Concepts shown:
- Class and Object
- Private Attributes
- Methods
- Deposit and Withdrawal operations
- Displaying account details
"""

class BankAccount:
    def __init__(self, accountNumber: str, balance: float):
        self.__accountNumber = accountNumber  # private attribute
        self.__balance = balance              # private attribute

    # Method to deposit money
    def deposit(self, amount: float) -> None:
        self.__balance += amount

    # Method to withdraw money
    def withdraw(self, amount: float) -> None:
        if self.__balance < amount:
            print("Insufficient funds!")
        else:
            self.__balance -= amount

    # Method to display account details
    def displayDetails(self) -> None:
        print("Account Number : " + self.__accountNumber)
        print("Balance : {:.2f}".format(self.__balance))


# Driver code
if __name__ == "__main__":
    accountNumber = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))

    account = BankAccount(accountNumber, balance)

    addBalance = float(input("Enter deposit amount: "))
    account.deposit(addBalance)

    withdrawBalance = float(input("Enter withdrawal amount: "))
    account.withdraw(withdrawBalance)

    account.displayDetails()