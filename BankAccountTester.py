#Tester for bankAccountClass
import unitttest
from bankAccountTester import BankAccount
class TestBankAccount(unittest.TestCase):
    
    
    first = input("Enter First Name:")
    last = input("Enter Last Name:")
    BankAccount(first, last)
    
    #------------------------------------------------------------------------------------------------------------
    #This is where the information returns to user: First and Last Name, Bank Account Number, Balance
    BankAccount.getFirst()
    BankAccount.getLast()
    BankAccount.getAccountNumber()
    BankAccount.getBalance()
    BankAccount.listTransacation[]
    #------------------------------------------------------------------------------------------------------------
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()
