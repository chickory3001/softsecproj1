"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the BankAccount module.
Test each method with at least one unit test.
"""

import unittest
from CheckingAccount import CheckingAccount
from BankAccount import BankAccount
from transaction import Transaction

# Define TestCheckingAccount class by extending the unittest.TestCase class
# Tests the checking account class 
class TestCheckingAccount(unittest.TestCase):
    # Class constants.
    ACCOUNT1NUMBER = 1000
    ACCOUNT2NUMBER = 1001
    DEPOSIT1 = 100.0
    DEPOSIT2 = 150.0
    INVALIDWITHDRAWAL =  101.0
    VALIDWITHDRAWAL = 100.0
    DEBUG = False
    
    # The setup method creates two checking accounts. 
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
        #this class doesn't even use timesOverdrawn but test it anyway 
        self.assertEqual(self.account1.getTimesOverdrawn(),0)
        self.assertEqual(self.account2.getTimesOverdrawn(),0)
    
    #test asserts on preconditions 
    def test_constructor_asserts(self):
        if TestCheckingAccount.DEBUG:
            print('\n testing constructor assertions')
        
        # test type assertion
        with self.assertRaises(AssertionError):
            # using the bankaccount constructor to test a bad input, since CheckingAccount() 
            # always calls the BankAccount constructor with 'Checking', which is valid.
            # with intended use, the BankAccount constructor will always be called via subclasses
            BankAccount('401k',1003)
        BankAccount('Checking',1100)
        CheckingAccount(1009)
        
        #test number assertion
        with self.assertRaises(AssertionError):
            CheckingAccount('s')
        with self.assertRaises(AssertionError):
            CheckingAccount(900)
        CheckingAccount(1006)
        CheckingAccount(5000)
    
    # Test the __eq__ special method.
    def test_eq(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the equal special method")
            
        # Assert
        self.assertTrue(self.account1 == self.account1)
        self.assertFalse(self.account1 == self.account2)
    
    # Test the __lt__ special method.
    def test_lt(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the less than special method")
            
        # Assert
        self.assertTrue(self.account1 < self.account2)
        self.assertFalse(self.account2 < self.account1)
    
    # Test the __gt__ special method.
    def test_gt(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the greater than special method")
            
        # Assert
        self.assertTrue(self.account2 > self.account1)
        self.assertFalse(self.account1 > self.account2)
    
    # Test the __le__ special method.
    def test_le(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the less than or equal to special method")
            
        # Assert
        self.assertTrue(self.account1 <= self.account1)
        self.assertTrue(self.account1 <= self.account2)
        self.assertFalse(self.account2 <= self.account1)
    
    # Test the __ge__ special method.
    def test_ge(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the greater than or equal to special method")
            
        # Assert
        self.assertTrue(self.account2 >= self.account1)
        self.assertTrue(self.account2 >= self.account2)
        self.assertFalse(self.account1 >= self.account2)
    
    # Test the __ne__ special method.
    def test_ne(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the not equal special method")
            
        # Assert
        self.assertTrue(self.account1 != self.account2)
        self.assertFalse(self.account1 != self.account1)
    
    # The test_getBalance method tests the getBalance method.
    def test_getBalance(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the getBalance method")
            
        # test initial balance = 0 
        self.assertEqual(self.account1.getBalance(), 0.0)
        
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
        
        # test withdraw asserts 
        with self.assertRaises(AssertionError):
            self.account1.withdraw(-1)
        with self.assertRaises(AssertionError):
            self.account1.withdraw('s')
        
        # Assert withdrawing too much returns False.
        self.account1.deposit(TestCheckingAccount.DEPOSIT1)
        print('Expect Transaction Denied: ')
        self.assertFalse(self.account1.withdraw(TestCheckingAccount.INVALIDWITHDRAWAL))
        self.assertEqual(self.account1.getBalance(),TestCheckingAccount.DEPOSIT1)
        
        # Assert withdrawing normally returns True. 
        self.account2.deposit(TestCheckingAccount.DEPOSIT2)
        self.assertTrue(self.account2.withdraw(TestCheckingAccount.VALIDWITHDRAWAL))
        self.assertEqual(self.account2.getBalance(),TestCheckingAccount.DEPOSIT2 - TestCheckingAccount.VALIDWITHDRAWAL)

        # Assert withdrawing from a negative balance returns False.
        self.account3 = CheckingAccount(1010)
        # it's not possible to get a negative balance in a checking account (with intended use) (if withdraw works correctly)
        # so I will manually add a transaction to make the balance negative 
        self.account3._transactions.append(Transaction(100,'withdrawal',-100.0))
        self.assertTrue(self.account3.getBalance() == -100.0)
        self.assertFalse(self.account3.withdraw(TestCheckingAccount.VALIDWITHDRAWAL))
        self.assertEqual(self.account3.getBalance(), -100.0)
    
    #Testing the transfer method
    def test_transfer(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the transfer method")
        
        # Deposit money into account1 so it has funds to transfer
        self.account1.deposit(TestCheckingAccount.DEPOSIT1)
        self.account2.deposit(TestCheckingAccount.DEPOSIT2)
        
        # Perform transfer of 100 from account1 → account2
        amount = 100.0
        result = self.account2.transfer(self.account1, amount)  #Transfer money from one account to another
        
        # Testing that it is returned true
        self.assertTrue(result)
        
        # checking the balances between both accounts
        self.assertEqual(self.account1.getBalance(), TestCheckingAccount.DEPOSIT1 - amount)
        self.assertEqual(self.account2.getBalance(), TestCheckingAccount.DEPOSIT2 + amount)
        
        # test transfer that fails
        self.account3 = CheckingAccount(1008)
        print('Expect Transaction Denied: ')
        self.assertFalse(self.account1.transfer(self.account3,1000))
        
        #test 'is not same account' assertion 
        with self.assertRaises(AssertionError):
            self.account2.transfer(self.account2,1.0)
        
        # test assertion must be > 0 
        with self.assertRaises(AssertionError):
            self.account3.transfer(self.account1,-1)
        
        #test type assertion
        with self.assertRaises(AssertionError):
            self.account3.transfer(self.account1,'s') 
    
    #Testing the interest method
    def test_Interest(self):
        if TestCheckingAccount.DEBUG:
            print("\nTesting the interest method")
        
        self.account1.deposit(TestCheckingAccount.DEPOSIT1)
        self.account1.addInterest()
        
        #hardcoding the correct interest rate
        #rounding to 1 decimal place because of float inaccuracy 
        self.assertEqual(round(self.account1.getBalance(),1), round(TestCheckingAccount.DEPOSIT1 * 1.015,1))   
        
        # test assertion
        self.account3 = CheckingAccount(1010)
        # it's not possible to get a negative balance in a checking account (with intended use) (if withdraw works correctly)
        # so I will manually add a transaction to make the balance negative 
        self.account3._transactions.append(Transaction(100,'withdrawal',-100.0))
        self.assertTrue(self.account3.getBalance() == -100.0)
        with self.assertRaises(AssertionError):
            self.account3.addInterest()

if __name__ == "__main__":
    unittest.main()
