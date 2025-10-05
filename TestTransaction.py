""" 
Simple Unit Test Example using Python's unittest module and assertions
@author: John McManus
@date: December 05, 2024

Import the unittest module and the Transaction module
Test each method with at least one unit test
"""

import unittest
from transaction import Transaction

""" Define test testTransaction class by extending the unittest.TestCase class"""

class TestTransaction(unittest.TestCase):
    
    DEPOSIT = 2000   # Expected Deposit amount
    WITHDRAWL = 500  # Expected Withdrawl amount
    FIRST = 100      # Expected first transaction number
    TYPE = "deposit" # Expected Deposit transaction type
    DEBUG = True
    
    # The setup method creates three transactions
    def setUp(self):
        self.transaction1 = Transaction(101,"deposit", TestTransaction.DEPOSIT)
        self.transaction2 = Transaction(102, "withdrawal", TestTransaction.WITHDRAWL)
        self.transaction3 = Transaction(103, "interest")

    # The test_constructor method tests the constructor 
    def test_constructor(self):
        self.assertEqual(self.transaction1.getAmount(), TestTransaction.DEPOSIT)
        self.assertEqual(self.transaction1.getTType(), TestTransaction.TYPE)
        if TestTransaction.DEBUG:
            print("\nTesting the constructor") 
            print("The first transaction: ", self.transaction1)
            print(repr(self.transaction1))

    # Test the __eq__ special method 
    def test_eq(self):
        if TestTransaction.DEBUG:
            print("\nTesting the equal special method") 
        
        # Assert
        self.assertTrue(self.transaction1 == self.transaction1)  

    # Second test of the __eq__ special method    
    def test_eq_2(self):
        if TestTransaction.DEBUG:
            print("\nSecond test of the equal special method")
        
        # Assert
        self.assertFalse(self.transaction1 == self.transaction2)  

    # Test the __ne__ special method     
    def test_ne(self):
        if TestTransaction.DEBUG:
            print("\nTesting the not equal special method ")
            
        # Assert
        self.assertTrue(self.transaction1 != self.transaction2)

    # Second test of the __ne__ special method     
    def test_ne_2(self):
        if TestTransaction.DEBUG:
            print("\nSecond test of the not equal special method") 
         
         #Assert   
        self.assertFalse(self.transaction1 != self.transaction1)    

    # Test the __add__ special method 
    def test_add(self):
        
        if TestTransaction.DEBUG:
            print("\nTesting the addition special method")  
        
        # Act
        addTest = self.transaction1 + self.transaction1
        
        # Assert
        self.assertEqual(addTest, 4000)

    # Test the __sub__ special method 
    def test_sub(self):
        
        if TestTransaction.DEBUG:
            print("\nTesting the subtraction special method")
          
        # Act  
        subTest = self.transaction1 - self.transaction2
        
        # Assert
        self.assertEqual(subTest, 1500)   

    # Test the __sum__ special method     
    def test_sum(self):
         # Arrange
        listTransactions = [self.transaction1, self.transaction2, self.transaction3]
        
        # Act
        sumTest = sum(listTransactions)
        
        # Assert
        self.assertEqual(sumTest, (TestTransaction.DEPOSIT + TestTransaction.WITHDRAWL))
        
        if TestTransaction.DEBUG:
            print("\nTesting the sum special method %d" % sumTest) 

if __name__ == '__main__':
    unittest.main()