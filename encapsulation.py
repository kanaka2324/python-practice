class BankAccount:
    def __init__(self, account_number, balance):
         self.__account_number = account_number 
         self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
           self.__balance += amount
           print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
           print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def get_balance(self):
         return self.__balance




b = BankAccount(1211,5000) 

print(b.get_balance())