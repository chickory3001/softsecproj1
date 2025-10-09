"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the BankAccount module.
Test each method with at least one unit test.
"""

import unittest
from bankaccount import BankAccount

"""Define TestBankAccount class by extending the unittest.TestCase class."""

class TestBankAccount(unittest.TestCase):
    
    #first = input("Enter First Name:")
    #last = input("Enter Last Name:")
    #bankAccountNum = random(rndint(1000,1000000) #Chooses a random integer between 1,000 and 100,000
    #BankAccount(first, last, bankAccountNum)
    
    #------------------------------------------------------------------------------------------------
    #This is where the information returns to user: First and Last Name, Bank Account Number, Balance
    #BankAccount.getFirst()
    #BankAccount.getLast()
    #BankAccount.getAccountNumber()
    #BankAccount.getBalance()
    #BankAccount.listTransacation[]
    #------------------------------------------------------------------------------------------------
    
    DEPOSIT1 =   2600000000
    DEPOSIT2 = 106000000000
    WITHDRAWL =  3000000000
    FIRST = "Tim"
    LAST = "Apple"
    DEBUG = True
    
    # The setup method creates three bank accounts. 
    def setUp(self):
        self.bankAccount1 = BankAccount("Tim", "Apple")
        self.bankAccount2 = BankAccount("Billiam", "Gates")
        
    
    # The test_constructor method tests the constructor.
    def test_constructor(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the constructor")
            print("The first bank account: ", self.bankAccount1)
            print(repr(self.bankAccount1))
            
        self.assertEqual(self.bankAccount1.getFirst(), TestBankAccount.FIRST)
        self.assertEqual(self.bankAccount1.getLast(), TestBankAccount.LAST)
            
            
    # Test the __eq__ special method.
    def test_eq(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the equal special method")
            
        # Assert
        self.assertTrue(self.bankAccount1 == self.bankAccount1)
        
        
    # Second test of the __eq__ special method.
    def test_eq_2(self):
        if TestBankAccount.DEBUG:
            print("\nSecond test of the equal special method")
            
        # Assert
        self.assertFalse(self.bankAccount1 == self.bankAccount2)
        
        
    # Test the __ne__ special method.
    def test_ne(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the not equal special method")
            
        # Assert
        self.assertTrue(self.bankAccount1 != self.bankAccount2)
        
        
    # Second test of the __ne__ special method.
    def test_ne_2(self):
        if TestBankAccount.DEBUG:
            print("\nSecond test of the not equal special method")
            
        # Assert
        self.assertFalse(self.bankAccount1 != self.bankAccount1)
        
    
    # The test_deposit method tests the deposit method.
    def test_deposit(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the deposit and getBalance methods")
            
        self.bankAccount1.deposit(TestBankAccount.DEPOSIT1)
        self.bankAccount2.deposit(TestBankAccount.DEPOSIT2)
        
        # Assert (NO OTHER DEPOSITS HAVE BEEN MADE SO BALANCE SHOULD EQUAL THE CONSTANT)
        self.assertEqual(self.bankAccount1.getBalance(), TestBankAccount.DEPOSIT1)
        self.assertEqual(self.bankAccount2.getBalance(), TestBankAccount.DEPOSIT2)
    
    
    
if __name__ == "__main__":
    unittest.main()
