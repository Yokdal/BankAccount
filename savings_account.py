from Baez_Yosvel_BankAccountPythonClass import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate  
        self.print_customer_information()
    def add_interest(self):
        interest = self.current_balance * (self.interest_rate / 100)  
        self.current_balance += interest
        print(f"Hello {self.customer_name}! Your new balance is {self.current_balance}")
