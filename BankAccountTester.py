#Tester for bankAccountClass
import unitttest
from bankAccountTester import BankAccount
class TestBankAccount(unittest.TestCase):
    
    
    first = input("Enter First Name:")
    last = input("Enter Last Name:")
    balance = float(input("Enter the amount of money being deposited:"))
    bankaccount(first, last, balance)
    
    #------------------------------------------------------------------------------------------------------------
    #This is where the information returns to: First and Last Name, Bank Account Number, Balance
    BankAccount.getAccount()
    BankAccount.getBalance()
    #------------------------------------------------------------------------------------------------------------
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()
