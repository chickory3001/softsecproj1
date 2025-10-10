"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the BankAccount module.
Test each method with at least one unit test.
"""

import unittest
from BankAccount import BankAccount

"""Define TestBankAccount class by extending the unittest.TestCase class"""

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
    INVALIDWITHDRAWAL =  2600000250
    VALIDWITHDRAWAL = 50
    FIRST = "Tim"
    LAST = "Apple"
    DEBUG = False
    
    # The setup method creates two bank accounts. 
    def setUp(self):
        # print('setup')
        self.bankAccount1 = BankAccount("Tim", "Apple")
        self.bankAccount2 = BankAccount("Billiam", "Gates")
        
    # The test_constructor method tests the constructor.
    def test_constructor(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the constructor")
            print("The first bank account: ", self.bankAccount1)
            print(self.bankAccount1)
            
        self.assertEqual(self.bankAccount1.getFirst(), TestBankAccount.FIRST)
        self.assertEqual(self.bankAccount1.getLast(), TestBankAccount.LAST)
        
    #test asserts on preconditions 
    def test_constructor_asserts(self):
        if TestBankAccount.DEBUG:
            print('\n testing constructor assertions')

        # catch the expected assertion errors
        # if an assertion error isn't raised on any of these, the test will fail 
        with self.assertRaises(AssertionError):
            self.bankAccount1 = BankAccount('a'*30,'smith')
        with self.assertRaises(AssertionError):
            self.bankAccount2 = BankAccount('','smith')
        with self.assertRaises(AssertionError):
            self.bankAccount3 = BankAccount('!@#$%^&*','smith')
        with self.assertRaises(AssertionError):
            self.bankAccount4 = BankAccount(100,'smith')
        with self.assertRaises(AssertionError):
            self.bankAccount5 = BankAccount('henry','')
        with self.assertRaises(AssertionError):
            self.bankAccount6 = BankAccount('henry','a'*41)
        with self.assertRaises(AssertionError):
            self.bankAccount7 = BankAccount('henry','!@#$%')
        with self.assertRaises(AssertionError):
            self.bankAccount8 = BankAccount('henry',100)
        
    # test account number increment 
    def test_accountNumber(self):
        if TestBankAccount.DEBUG:
            print('\n testing account number increment')
        nextNumber = BankAccount._nextAccountNumber - 2
        self.assertEqual(self.bankAccount1.getAccountNumber(),nextNumber)
        nextNumber = BankAccount._nextAccountNumber - 1
        self.assertEqual(self.bankAccount2.getAccountNumber(),nextNumber)
    # Test the __eq__ special method.
    def test_eq(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the equal special method")
            
        # Assert
        self.assertTrue(self.bankAccount1 == self.bankAccount1)
        
    # Test the __lt__ special method.
    def test_lt(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the less than special method")
            
        # Assert
        self.assertTrue(self.bankAccount1 < self.bankAccount2)
        
    # Test the __gt__ special method.
    def test_gt(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the greater than special method")
            
        # Assert
        self.assertTrue(self.bankAccount2 > self.bankAccount1)
        
    # Test the __le__ special method.
    def test_le(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the less than or equal to special method")
            
        # Assert
        self.assertTrue(self.bankAccount1 <= self.bankAccount1)
        
    # Test the __ge__ special method.
    def test_ge(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the greater than or equal to special method")
            
        # Assert
        self.assertTrue(self.bankAccount2 >= self.bankAccount1)
        
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
    
    # The test_getFirst method tests the getFirst method.
    def test_getFirst(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the getFirst method")
            
        # Assert
        self.assertEqual(self.bankAccount1.getFirst(), TestBankAccount.FIRST)
        
    # The test_getLast method tests the getLast method.
    def test_getLast(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the getLast method")
            
        # Assert
        self.assertEqual(self.bankAccount1.getLast(), TestBankAccount.LAST)
        
    # The test_getBalance method tests the getBalance method.
    def test_getBalance(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the getBalance method")
            
        # test initial balance = 0 
        self.assertEqual(self.bankAccount1.getBalance(), 0)

        #test that a deposit increases balance appropriately
        self.bankAccount1.deposit(TestBankAccount.DEPOSIT1)
        self.assertEqual(self.bankAccount1.getBalance(),TestBankAccount.DEPOSIT1)

        #test that a withdrawal decreases balance appropriately
        self.bankAccount1.withdraw(TestBankAccount.VALIDWITHDRAWAL)
        self.assertEqual(self.bankAccount1.getBalance(),TestBankAccount.DEPOSIT1 - TestBankAccount.VALIDWITHDRAWAL)
        
    # The test_deposit method tests the deposit method.
    def test_deposit(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the deposit and getBalance methods")
            
        self.bankAccount1.deposit(TestBankAccount.DEPOSIT1)
        self.bankAccount2.deposit(TestBankAccount.DEPOSIT2)
        
        # Assert (NO OTHER DEPOSITS HAVE BEEN MADE SO BALANCE SHOULD EQUAL THE CONSTANT)
        self.assertEqual(self.bankAccount1.getBalance(), TestBankAccount.DEPOSIT1)
        self.assertEqual(self.bankAccount2.getBalance(), TestBankAccount.DEPOSIT2)
    
    # The test_withdraw method tests the withdraw method.
    def test_withdraw(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the withdraw method")
            
        # Assert withdrawing negative amounts results in an error.
        with self.assertRaises(AssertionError):
            self.bankAccount1.withdraw(-1)
        
        # Assert withdrawing too much returns False.
        self.assertFalse(self.bankAccount1.withdraw(TestBankAccount.INVALIDWITHDRAWAL))
        
        # Assert withdrawing normally returns True. 
        self.bankAccount1.deposit(TestBankAccount.DEPOSIT1)
        self.assertTrue(self.bankAccount1.withdraw(TestBankAccount.VALIDWITHDRAWAL))

        self.bankAccount2.deposit(1000)
        self.bankAccount2.withdraw(1100)
        self.assertEqual(self.bankAccount2.getBalance(),-100 - BankAccount.OVERDRAFT_FEE)
        self.assertEqual(self.bankAccount2.getTimesOverdrawn(),1)
    
    #Testing the transfer method
    def test_transfer(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the transfer method")
        
        # Deposit money into bankAccount1 so it has funds to transfer
        self.bankAccount1.deposit(TestBankAccount.DEPOSIT1)
        self.bankAccount2.deposit(TestBankAccount.DEPOSIT2)
        
        # Checks the balances before the transfer is done
        initialBalance1 = self.bankAccount1.getBalance()
        initialBalance2 = self.bankAccount2.getBalance()
        
        # Perform transfer of 500 from bankAccount1 → bankAccount2
        amount = 500.0
        result = self.bankAccount2.transfer(self.bankAccount1, amount)  #Transfer money from one account to another
        
        # Testing that it is returned true
        self.assertTrue(result)
        
        # Updating the balances between both accounts
        self.assertEqual(self.bankAccount1.getBalance(), initialBalance1 - amount)
        self.assertEqual(self.bankAccount2.getBalance(), initialBalance2 + amount)

        # test transfer that fails
        self.bankAccount3 = BankAccount('e','e')
        self.assertFalse(self.bankAccount1.transfer(self.bankAccount3,1000))

        # test assertion must be > 0 
        with self.assertRaises(AssertionError):
            self.bankAccount3.transfer(self.bankAccount1,-1)

    #Testing the interest method
    def test_Interest(self):
        if TestBankAccount.DEBUG:
            print("\nTesting the interest method")
        
        self.bankAccount1.deposit(100)
        self.bankAccount1.addInterest()
        self.assertEqual(self.bankAccount1.getBalance(), 107.5)   #Testing if the interest added the appropriate amount

    
if __name__ == "__main__":
    unittest.main()
