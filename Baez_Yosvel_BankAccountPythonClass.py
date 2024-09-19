"""
Author:Yosvel Baez
Date: 09/03/2024
"""
# Below is the code for Bank Account Class
class BankAccount:
    # This is an attribute under the BankAccount Class called "title_of_bank"
    title_of_bank = "Money Bank"

    # This is a constructor method of the BankAccount Class which holds all the details of the customer(in the rubric it is called an instance attribute)
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  
        self.__routing_number = routing_number  

    # Below this line is the deposit method which is representing the deposit transaction
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(self.current_balance)
            return self.current_balance

    # Below this line is the withdraw method which is representing the withdraw transaction
    def withdraw(self, amount):
        if amount > 0:
            if self.current_balance - amount >= self.minimum_balance:
                self.current_balance -= amount
                print(f"{amount} was withdrawn. Your new balance is {self.current_balance}")
            else:
                print(f"We're sorry but you can't withdraw {amount}, it looks like you don't have that much money in your account. Your current balance is {self.current_balance}")
                return self.current_balance
        else:
            print("Please enter a valid amount to withdraw")

        return None

    def print_customer_information(self):
        print(f"Bank: {self.title_of_bank}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.__routing_number}")

    def print_account_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self._BankAccount__routing_number}")

# Below this line here are some test cases
#acc1 = BankAccount("Yosvel Baez", 930, 400, 123456789, 987654321)
#acc2 = BankAccount("Nick Viscuise", 950, 375, 987654321, 123456789)

# Below this line is the deposit and withdraw methods tested on acc1
#acc1.deposit(500)
#acc1.withdraw(200)
#acc1.print_customer_information()

# Below this line is the deposit and withdraw methods tested on acc2
#acc2.deposit(500)
#acc2.withdraw(200)
#acc2.print_customer_information()