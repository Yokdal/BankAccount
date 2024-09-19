from Baez_Yosvel_BankAccountPythonClass import BankAccount

class CheckingAccount(BankAccount):
    
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit  
        self.print_customer_information()
    def transfer(self, amount):
        if amount > self.transfer_limit:
            print(f"Transfer of {amount} exceeds limit of {self.transfer_limit}")
        else:
            result = self.withdraw(amount)
            if result is not None:
                print(f"Transferred: {amount}. New balance: {self.current_balance}")
