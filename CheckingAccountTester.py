"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the BankAccount module.
Test each method with at least one unit test.
"""

import unittest
from CheckingAccount import CheckingAccount
from BankAccount import BankAccount
"""Define TestCheckingAccount class by extending the unittest.TestCase class"""

class TestCheckingAccount(unittest.TestCase):
    # Class constants.
    ACCOUNT1NUMBER = 1000
    ACCOUNT2NUMBER = 1001
    DEPOSIT1 =   2600000000
    DEPOSIT2 = 106000000000
    INVALIDWITHDRAWAL =  2600000250
    VALIDWITHDRAWAL = 50
    DEBUG = False
    
    # The setup method creates two checkint accounts. 
    def setUp(self):
        self.account1 = CheckingAccount(1000)
        self.account2 = CheckingAccount(1001)
    
    # The test_constructor method tests the constructor.
    def test_constructor(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the constructor")
            print("The first bank account: ", self.account1)
        
        self.assertEqual(self.account1.getAccountNumber(), TestCheckingAccount.ACCOUNT1NUMBER)
        self.assertEqual(self.account2.getAccountNumber(), TestCheckingAccount.ACCOUNT2NUMBER)
        self.assertEqual(self.account1.getType(),'Checking')
        self.assertEqual(self.account2.getType(),'Checking')
        self.assertEqual(self.account1.getTransactions(),[])
        self.assertEqual(self.account2.getTransactions(),[])
        self.assertEqual(self.account1.getTimesOverdrawn(),0)
        self.assertEqual(self.account2.getTimesOverdrawn(),0)
    
    #test asserts on preconditions 
    def test_constructor_asserts(self):
        if TestCheckingAccount.DEBUG:
            print('\n testing constructor assertions')
        
        # catch the expected assertion errors
        # if an assertion error isn't raised on any of these, the test will fail 
        with self.assertRaises(AssertionError):
            # using the bankaccount constructor to test a bad input, since CheckingAccount() 
            # always calls the BankAccount constructor with 'Checking', which is valid.
            # with intended use, a BankAccount class will only ever be created via subclasses
            BankAccount('401k',1003)
        with self.assertRaises(AssertionError):
            CheckingAccount('s')
        with self.assertRaises(AssertionError):
            CheckingAccount('900')
    
    # test account number increment 
    def test_accountNumber(self):
        if TestCheckingAccount.DEBUG:
            print('\n testing account number increment')
        nextNumber = BankAccount._nextAccountNumber - 2
        self.assertEqual(self.account1.getAccountNumber(),nextNumber)
        nextNumber = BankAccount._nextAccountNumber - 1
        self.assertEqual(self.account2.getAccountNumber(),nextNumber)
    
    # Test the __eq__ special method.
    def test_eq(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the equal special method")
            
        # Assert
        self.assertTrue(self.account1 == self.account1)
    
    # Test the __lt__ special method.
    def test_lt(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the less than special method")
            
        # Assert
        self.assertTrue(self.account1 < self.account2)
    
    # Test the __gt__ special method.
    def test_gt(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the greater than special method")
            
        # Assert
        self.assertTrue(self.account2 > self.account1)
    
    # Test the __le__ special method.
    def test_le(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the less than or equal to special method")
            
        # Assert
        self.assertTrue(self.account1 <= self.account1)
    
    # Test the __ge__ special method.
    def test_ge(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the greater than or equal to special method")
            
        # Assert
        self.assertTrue(self.account2 >= self.account1)
    
    # Second test of the __eq__ special method.
    def test_eq_2(self):
        if TestCheckingAccount.DEBUG:
            print("\nSecond test of the equal special method")
            
        # Assert
        self.assertFalse(self.account1 == self.account2)
    
    # Test the __ne__ special method.
    def test_ne(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the not equal special method")
            
        # Assert
        self.assertTrue(self.account1 != self.account2)
    
    # Second test of the __ne__ special method.
    def test_ne_2(self):
        if TestCheckingAccount.DEBUG:
            print("\nSecond test of the not equal special method")
            
        # Assert
        self.assertFalse(self.account1 != self.account1)
    
    # The test_getFirst method tests the getFirst method.
    def test_getFirst(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the getFirst method")
            
        # Assert
        self.assertEqual(self.account1.getFirst(), TestCheckingAccount.FIRST)
    
    # The test_getLast method tests the getLast method.
    def test_getLast(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the getLast method")
            
        # Assert
        self.assertEqual(self.account1.getLast(), TestCheckingAccount.LAST)
    
    # The test_getBalance method tests the getBalance method.
    def test_getBalance(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the getBalance method")
            
        # test initial balance = 0 
        self.assertEqual(self.account1.getBalance(), 0)

        #test that a deposit increases balance appropriately
        self.account1.deposit(TestCheckingAccount.DEPOSIT1)
        self.assertEqual(self.account1.getBalance(),TestCheckingAccount.DEPOSIT1)

        #test that a withdrawal decreases balance appropriately
        self.account1.withdraw(TestCheckingAccount.VALIDWITHDRAWAL)
        self.assertEqual(self.account1.getBalance(),TestCheckingAccount.DEPOSIT1 - TestCheckingAccount.VALIDWITHDRAWAL)
    
    # The test_deposit method tests the deposit method.
    def test_deposit(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the deposit and getBalance methods")
            
        self.account1.deposit(TestCheckingAccount.DEPOSIT1)
        self.account2.deposit(TestCheckingAccount.DEPOSIT2)
        
        # Assert (NO OTHER DEPOSITS HAVE BEEN MADE SO BALANCE SHOULD EQUAL THE CONSTANT)
        self.assertEqual(self.account1.getBalance(), TestCheckingAccount.DEPOSIT1)
        self.assertEqual(self.account2.getBalance(), TestCheckingAccount.DEPOSIT2)
    
    # The test_withdraw method tests the withdraw method.
    def test_withdraw(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the withdraw method")
            
        # Assert withdrawing negative amounts results in an error.
        with self.assertRaises(AssertionError):
            self.account1.withdraw(-1)
        
        # Assert withdrawing too much returns False.
        self.assertFalse(self.account1.withdraw(TestCheckingAccount.INVALIDWITHDRAWAL))
        
        # Assert withdrawing normally returns True. 
        self.account1.deposit(TestCheckingAccount.DEPOSIT1)
        self.assertTrue(self.account1.withdraw(TestCheckingAccount.VALIDWITHDRAWAL))

        self.account2.deposit(1000)
        self.account2.withdraw(1100)
        self.assertEqual(self.account2.getBalance(),-100 - BankAccount.OVERDRAFT_FEE)
        self.assertEqual(self.account2.getTimesOverdrawn(),1)
    
    #Testing the transfer method
    def test_transfer(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the transfer method")
        
        # Deposit money into account1 so it has funds to transfer
        self.account1.deposit(TestCheckingAccount.DEPOSIT1)
        self.account2.deposit(TestCheckingAccount.DEPOSIT2)
        
        # Checks the balances before the transfer is done
        initialBalance1 = self.account1.getBalance()
        initialBalance2 = self.account2.getBalance()
        
        # Perform transfer of 500 from account1 → account2
        amount = 500.0
        result = self.account2.transfer(self.account1, amount)  #Transfer money from one account to another
        
        # Testing that it is returned true
        self.assertTrue(result)
        
        # Updating the balances between both accounts
        self.assertEqual(self.account1.getBalance(), initialBalance1 - amount)
        self.assertEqual(self.account2.getBalance(), initialBalance2 + amount)

        # test transfer that fails
        self.bankAccount3 = BankAccount('e','e')
        self.assertFalse(self.account1.transfer(self.bankAccount3,1000))

        # test assertion must be > 0 
        with self.assertRaises(AssertionError):
            self.bankAccount3.transfer(self.account1,-1)

    #Testing the interest method
    def test_Interest(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the interest method")
        
        self.account1.deposit(100)
        self.account1.addInterest()
        self.assertEqual(self.account1.getBalance(), 107.5)   #Testing if the interest added the appropriate amount


if __name__ == "__main__":
    unittest.main()
