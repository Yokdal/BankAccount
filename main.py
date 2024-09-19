#this is my importing of the savings account and checking account files
from savings_account import SavingsAccount
from checking_account import CheckingAccount

def main():
    # These are two instances of SavingsAccount
    savings1 = SavingsAccount("Yosvel", 1000, 500, 12345, 67890, 2)
    savings2 = SavingsAccount("Nicolas", 2000, 500, 54321, 98765, 3)

    # Perform interest addition with savings accounts
    savings1.add_interest()
    savings2.add_interest()

    # Create two instances of CheckingAccount
    
    checking1 = CheckingAccount("Theodora", 2000, 200, 10, 12312525, 23446797)
    checking2 = CheckingAccount("Eleanore", 9000, 400, 14324564, 6846575463, 245257668)

    # Perform transfer with checking accounts 
    checking1.transfer(200)
    checking2.transfer(1200) 

if __name__ == "__main__":
    main()
