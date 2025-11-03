"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the BankAccount module.
Test each method with at least one unit test.
"""

import unittest
from SavingsAccount import SavingsAccount
from BankAccount import BankAccount
from transaction import Transaction

# Define TestSavingsAccount class by extending the unittest.TestCase class
# Tests the savings account class 
class TestSavingsAccount(unittest.TestCase):
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
        self.account1 = SavingsAccount(1000)
        self.account2 = SavingsAccount(1001)
    
    # The test_constructor method tests the constructor.
    def test_constructor(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the constructor")
            print("The first bank account: ", self.account1)
        
        self.assertEqual(self.account1.getAccountNumber(), TestSavingsAccount.ACCOUNT1NUMBER)
        self.assertEqual(self.account2.getAccountNumber(), TestSavingsAccount.ACCOUNT2NUMBER)
        self.assertEqual(self.account1.getType(),'Savings')
        self.assertEqual(self.account2.getType(),'Savings')
        self.assertEqual(self.account1.getTransactions(),[])
        self.assertEqual(self.account2.getTransactions(),[])
        self.assertEqual(self.account1.getTimesOverdrawn(),0)
        self.assertEqual(self.account2.getTimesOverdrawn(),0)
    
    #test asserts on preconditions 
    def test_constructor_asserts(self):
        if TestSavingsAccount.DEBUG:
            print('\n testing constructor assertions')
        
        # test type assertion
        with self.assertRaises(AssertionError):
            # using the bankaccount constructor to test a bad input, since SavingsAccount() 
            # always calls the BankAccount constructor with 'Savings', which is valid.
            # with intended use, the BankAccount constructor will always be called via subclasses
            BankAccount('401k',1003)
        BankAccount('Savings',1100)
        SavingsAccount(1009)
        
        #test number assertion
        with self.assertRaises(AssertionError):
            SavingsAccount('s')
        with self.assertRaises(AssertionError):
            SavingsAccount(900)
        SavingsAccount(1006)
        SavingsAccount(5000)
    
    # Test the __eq__ special method.
    def test_eq(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the equal special method")
            
        # Assert
        self.assertTrue(self.account1 == self.account1)
        self.assertFalse(self.account1 == self.account2)
    
    # Test the __lt__ special method.
    def test_lt(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the less than special method")
            
        # Assert
        self.assertTrue(self.account1 < self.account2)
        self.assertFalse(self.account2 < self.account1)
    
    # Test the __gt__ special method.
    def test_gt(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the greater than special method")
            
        # Assert
        self.assertTrue(self.account2 > self.account1)
        self.assertFalse(self.account1 > self.account2)
    
    # Test the __le__ special method.
    def test_le(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the less than or equal to special method")
            
        # Assert
        self.assertTrue(self.account1 <= self.account1)
        self.assertTrue(self.account1 <= self.account2)
        self.assertFalse(self.account2 <= self.account1)
    
    # Test the __ge__ special method.
    def test_ge(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the greater than or equal to special method")
            
        # Assert
        self.assertTrue(self.account2 >= self.account1)
        self.assertTrue(self.account2 >= self.account2)
        self.assertFalse(self.account1 >= self.account2)
    
    # Test the __ne__ special method.
    def test_ne(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the not equal special method")
            
        # Assert
        self.assertTrue(self.account1 != self.account2)
        self.assertFalse(self.account1 != self.account1)
    
    # The test_getBalance method tests the getBalance method.
    def test_getBalance(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the getBalance method")
        
        # test initial balance = 0 
        self.assertEqual(self.account1.getBalance(), 0.0)
        
        #test that a deposit increases balance appropriately
        self.account1.deposit(TestSavingsAccount.DEPOSIT1)
        self.assertEqual(self.account1.getBalance(),TestSavingsAccount.DEPOSIT1)
        
        #test that a withdrawal decreases balance appropriately
        self.account1.withdraw(TestSavingsAccount.VALIDWITHDRAWAL)
        self.assertEqual(self.account1.getBalance(),TestSavingsAccount.DEPOSIT1 - TestSavingsAccount.VALIDWITHDRAWAL)
    
    # The test_deposit method tests the deposit method.
    def test_deposit(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the deposit and getBalance methods")
        
        self.account1.deposit(TestSavingsAccount.DEPOSIT1)
        self.account2.deposit(TestSavingsAccount.DEPOSIT2)
        
        # Assert (NO OTHER DEPOSITS HAVE BEEN MADE SO BALANCE SHOULD EQUAL THE CONSTANT)
        self.assertEqual(self.account1.getBalance(), TestSavingsAccount.DEPOSIT1)
        self.assertEqual(self.account2.getBalance(), TestSavingsAccount.DEPOSIT2)
    
    # The test_withdraw method tests the withdraw method.
    def test_withdraw(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the withdraw method")
        
        # test withdraw asserts 
        with self.assertRaises(AssertionError):
            self.account1.withdraw(-1)
        with self.assertRaises(AssertionError):
            self.account1.withdraw('s')
        
        # Assert withdrawing too much returns False.
        self.account1.deposit(TestSavingsAccount.DEPOSIT1)
        print('Expect Transaction Denied: ')
        self.assertFalse(self.account1.withdraw(TestSavingsAccount.DEPOSIT1 + 251))
        self.assertEqual(self.account1.getBalance(),TestSavingsAccount.DEPOSIT1)
        
        #ensure withdrawing with a balance = 0 is denied 
        self.account3 = SavingsAccount(1004)
        self.assertEqual(self.account3.getBalance(), 0)
        print('Expect Transaction Denied: ')
        self.assertFalse(self.account3.withdraw(1))
        
        #ensure withdrawing with a negative balance is denied 
        self.account3.deposit(1)
        print('Expect Account has been overdrawn:')
        self.account3.withdraw(2)
        self.assertTrue(self.account3.getBalance() < 0)
        print('Expect Transaction Denied: ')
        self.assertFalse(self.account3.withdraw(1))
        
        # Assert withdrawing normally returns True. 
        self.account2.deposit(TestSavingsAccount.DEPOSIT2)
        self.assertTrue(self.account2.withdraw(TestSavingsAccount.VALIDWITHDRAWAL))
        self.assertEqual(self.account2.getBalance(),TestSavingsAccount.DEPOSIT2 - TestSavingsAccount.VALIDWITHDRAWAL)
    
    # tests the overdraft functionality 
    def test_overdraft(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the overdraft functionality")
        deposit = 50
        overdraftwithdrawal = 60
        
        # test first overdraft 
        self.assertEqual(self.account1.getTimesOverdrawn(),0)
        self.account1.deposit(deposit)
        print('Expect Account has been overdrawn:')
        self.assertTrue(self.account1.withdraw(overdraftwithdrawal))
        self.assertEqual(self.account1.getTimesOverdrawn(),1)
        self.assertEqual(self.account1.getBalance(),  deposit - overdraftwithdrawal - SavingsAccount.OVERDRAFT_FEE1)
        
        # test second overdraft
        self.account1.deposit(abs(self.account1.getBalance()) + deposit) # set balance back to deposit 
        print('Expect Account has been overdrawn:')
        self.assertTrue(self.account1.withdraw(overdraftwithdrawal))
        self.assertEqual(self.account1.getTimesOverdrawn(),2)
        self.assertEqual(self.account1.getBalance(), deposit - overdraftwithdrawal - SavingsAccount.OVERDRAFT_FEE2)
        
        #test third overdraft
        self.account1.deposit(abs(self.account1.getBalance()) + deposit) # set balance back to deposit 
        print('Expect Account has been overdrawn:')
        self.assertTrue(self.account1.withdraw(overdraftwithdrawal))
        self.assertEqual(self.account1.getTimesOverdrawn(),3)
        self.assertEqual(self.account1.getBalance(), deposit - overdraftwithdrawal - SavingsAccount.OVERDRAFT_FEE3)
        
        #ensure withdrawals after 3rd overdraft are denied 
        self.account1.deposit(abs(self.account1.getBalance()) + deposit) # set balance back to deposit 
        print("Expect Transaction Denied: ")
        self.assertFalse(self.account1.withdraw(1))
        
        #ensure overdraft counter is reduced by 1 when the balance reaches at least 100$ 
        self.account1.deposit(100 - self.account1.getBalance()) # set balance to 100 
        self.assertEqual(self.account1.getBalance(), 100)
        self.assertEqual(self.account1.getTimesOverdrawn(),2)
        
        #ensure overdraft counter gets reset to 0 when the balance reaches 10,000
        self.account1.deposit(9900)
        self.assertEqual(self.account1.getBalance(), 10000)
        self.assertEqual(self.account1.getTimesOverdrawn(),0)
    
    #Testing the transfer method
    def test_transfer(self):
        if TestSavingsAccount.DEBUG:
            print("\nTesting the transfer method")
        
        # Deposit money into account1 so it has funds to transfer
        self.account1.deposit(TestSavingsAccount.DEPOSIT1)
        self.account2.deposit(TestSavingsAccount.DEPOSIT2)
        
        # Perform transfer of 100 from account1 → account2
        amount = 100.0
        result = self.account2.transfer(self.account1, amount)  #Transfer money from one account to another
        
        # Testing that it is returned true
        self.assertTrue(result)
        
        # checking the balances between both accounts
        self.assertEqual(self.account1.getBalance(), TestSavingsAccount.DEPOSIT1 - amount)
        self.assertEqual(self.account2.getBalance(), TestSavingsAccount.DEPOSIT2 + amount)
        
        # test transfer that fails
        self.account3 = SavingsAccount(1008)
        print('Expect Transaction Denied: ')
        self.assertFalse(self.account1.transfer(self.account3,1000))
        
        # test transfer that triggers overdraft 
        print('Expect Account has been overdrawn:')
        self.account3.deposit(TestSavingsAccount.DEPOSIT1)
        self.assertTrue(self.account1.transfer(self.account3,TestSavingsAccount.INVALIDWITHDRAWAL))
        self.assertEqual(self.account3.getTimesOverdrawn(),1)
        
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
        if TestSavingsAccount.DEBUG:
            print("\nTesting the interest method")
        
        self.account1.deposit(TestSavingsAccount.DEPOSIT1)
        self.account1.addInterest()
        
        #hardcoding the correct interest rate
        #rounding to 1 decimal place because of float inaccuracy 
        self.assertEqual(round(self.account1.getBalance(),1), round(TestSavingsAccount.DEPOSIT1 * 1.04,1))   
        
        # test assertion
        self.account3 = SavingsAccount(1010)
        self.account3.deposit(100)
        print('Expect Account has been overdrawn:')
        self.account3.withdraw(101)
        self.assertTrue(self.account3.getBalance() == -21.0)
        with self.assertRaises(AssertionError):
            self.account3.addInterest()

if __name__ == "__main__":
    unittest.main()
