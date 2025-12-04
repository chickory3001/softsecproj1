"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the Client module.
Test each method with at least one unit test.
"""

import unittest
from Client import Client
from Address import Address
from FirstName import FirstName
from LastName import LastName

# Class to test the client class 
class TestClient(unittest.TestCase):
    
    # Constants
    FIRSTNAME = FirstName('timmy')
    LASTNAME = LastName('smith')
    PHONE= "9123456789"
    ADDRESS = Address('304 timmy Drive','Glen alLen','vA')
    INITIALTYPE = 'c'
    CLIENTNUMBER = 100
    DEBUG = True

    # The setup method creates a client
    def setUp(self):
        self.client1 = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)
    
    # Teardown resets the first client number 
    def tearDown(self):
        Client._nextClientNumber = 100
    
    # Tests constuctor   
    def test_constructor(self):
        if TestClient.DEBUG:
            print("\nTesting the constructor")
        
        self.assertEqual(self.client1._first, TestClient.FIRSTNAME)
        self.assertEqual(self.client1._last, TestClient.LASTNAME)
        self.assertEqual(self.client1._phone, TestClient.PHONE)
        self.assertEqual(self.client1._address, TestClient.ADDRESS)
        self.assertEqual(self.client1._clientNumber, TestClient.CLIENTNUMBER)
        self.assertEqual(self.client1._accounts[0]._type, TestClient.INITIALTYPE)
        self.assertEqual(len(self.client1._accounts), 1)

        client2 = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, 's')
        self.assertEqual(client2._accounts[0]._type, 's')

    # Testing assertions in the constructor 
    def test_constructor_asserts(self):
        if TestClient.DEBUG:
            print("\nTesting the constructor assertions")
        
        # Test first name assert 
        with self.assertRaises(AssertionError):
            client = Client(12312321,TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)
        
        # Test last name assert 
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,12312321,TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)
        
        # Test phone number assert 
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,9123456789,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,'a'*10,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,'a'*11,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,'0123456789',TestClient.ADDRESS, TestClient.INITIALTYPE)
        
        # Test address assert 
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,TestClient.PHONE,'ssssssss', TestClient.INITIALTYPE)
        
        # Test inital account type assert 
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, 123131)
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, 'a')

    # Testing opening an account               
    def test_open_account(self):
        if TestClient.DEBUG:
            print("\nTesting the openAccount method")
        
        self.assertEqual(len(self.client1._accounts), 1)
        self.assertEqual(self.client1._accounts[0]._accountNumber,1000)

        # Testing a valid checking account opening
        self.client1.openAccount("c")
        self.assertEqual(len(self.client1._accounts), 2)
        self.assertEqual(self.client1._accounts[1]._type, "c")
        self.assertEqual(self.client1._accounts[1]._accountNumber,1001)

        # Testing a valid savings account opening
        self.client1.openAccount("s")
        self.assertEqual(len(self.client1._accounts), 3)
        self.assertEqual(self.client1._accounts[2]._type, "s")
        self.assertEqual(self.client1._accounts[2]._accountNumber,1002)

        # Testing that having the type argument not be of type string leads to assert error
        with self.assertRaises(AssertionError):
            self.client1.openAccount(10)
        self.assertEqual(len(self.client1._accounts), 3)
        
        # Testing that having the type argument not be either "c" or "s" leads to assert error
        with self.assertRaises(AssertionError):
            self.client1.openAccount("Invalid")
        self.assertEqual(len(self.client1._accounts), 3)
    
    # Testing closing an account   
    def test_close_account(self):
        if TestClient.DEBUG:
            print("\nTesting the closeAccount method")
        
        # 1 is the checking account created from the constructor
        self.assertEqual(len(self.client1._accounts), 1)

        # Test assert for trying to close an account with the number not being an int
        with self.assertRaises(AssertionError):
            self.client1.closeAccount("Invalid")

        # Test assert for trying to close an account with the number being less than 1000
        with self.assertRaises(AssertionError):
            self.client1.closeAccount(10)

        # Attempt to close a nonexistant account, should return False
        result = self.client1.closeAccount(9999)
        self.assertEqual(result, False)

        # Adding a 2nd account so we can close it with no balance
        self.client1.openAccount("c")
        self.assertEqual(len(self.client1._accounts), 2)

        # Closing 2nd account with a balance of zero, should return True
        result = self.client1.closeAccount(self.client1._accounts[1].getAccountNumber())
        self.assertEqual(result, True)
        self.assertEqual(len(self.client1._accounts),1)

        # Adding an account so we can close it with a positive balance
        self.client1.openAccount("c")
        self.assertEqual(len(self.client1._accounts), 2)
        self.client1._accounts[1].deposit(1000.0)

        # Closing the account with a positive balance, should return True
        result = self.client1.closeAccount(self.client1._accounts[1].getAccountNumber())
        self.assertEqual(result, True)
        self.assertEqual(len(self.client1._accounts),1)

        # Adding an account so we can close it with a negative balance
        self.client1.openAccount("s")
        self.assertEqual(len(self.client1._accounts), 2)
        self.client1._accounts[1].deposit(1)
        self.client1._accounts[1].withdraw(10)
        self.assertTrue(self.client1._accounts[1].getBalance() < 0)

        # Closing the account with a negative balance, should return False
        result = self.client1.closeAccount(self.client1._accounts[1].getAccountNumber())
        self.assertEqual(result, False)
        self.assertEqual(len(self.client1._accounts),2)

if __name__ == "__main__":
    unittest.main()
