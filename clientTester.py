"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the Client module.
Test each method with at least one unit test.
"""

import unittest
from Client import Client
from Address import Address

class TestClient(unittest.TestCase):
    #Constants
    FIRSTNAME = 'timmy'
    LASTNAME = 'smith'
    PHONE= "9123456789"
    ADDRESS = Address('304 timmy Drive','Glen alLen','vA')
    INITIALTYPE = 'c'
    CLIENTNUMBER = 1000 
    DEBUG = False

    # The setup method creates a client
    def setUp(self):
        self.client1 = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)

    #Tests constuctor   
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
        self.assertEqual(self.client1._accounts[0]._type, 's')

    # testing assertions in the constructor 
    def test_constructor_asserts(self):
        if TestClient.DEBUG:
            print("\nTesting the constructor assertions")
        
        # test first name assert 
        with self.assertRaises(AssertionError):
            client = Client(12312321,TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client('whatever\n',TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client('',TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client('a'*26,TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)
        # test last name assert 
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,12312321,TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,'whatever\n',TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,'',TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,'a'*41,TestClient.PHONE,TestClient.ADDRESS, TestClient.INITIALTYPE)
        # test phone number assert 
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,9123456789,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,'a'*10,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,'a'*11,TestClient.ADDRESS, TestClient.INITIALTYPE)
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,'0123456789',TestClient.ADDRESS, TestClient.INITIALTYPE)
        # test address assert 
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,TestClient.PHONE,'ssssssss', TestClient.INITIALTYPE)
        # test inital account type assert 
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, 123131)
        with self.assertRaises(AssertionError):
            client = Client(TestClient.FIRSTNAME,TestClient.LASTNAME,TestClient.PHONE,TestClient.ADDRESS, 'a')

    # Testing opening an account               
    def test_open_account(self):
        if TestClient.DEBUG:
            print("\nTesting the openAccount method")
        
        #Testing a valid checking account opening
        self.client1.openAccount("c")
        self.assertEqual(len(self.client1._accounts), 2)
        self.assertEqual(self.client1._accounts[1]._type, "c")

        #Testing a valid savings account opening
        self.client1.openAccount("s")
        self.assertEqual(len(self.client1._accounts), 3)
        self.assertEqual(self.client1._accounts[2]._type, "s")

        #Testing that having the type argument not be of type string leads to assert error
        with self.assertRaises(AssertionError):
            self.client1.openAccount(10)
        self.assertEqual(len(self.client1._accounts), 3)
        
        #Testing that having the type argument not be either "c" or "s" leads to assert error
        with self.assertRaises(AssertionError):
            self.client1.openAccount("Invalid")
        self.assertEqual(len(self.client1._accounts), 3)
    
    # Testing closing an account   
    def test_close_account(self):
        if TestClient.DEBUG:
            print("\nTesting the closeAccount method")
        #1 is the checking account created from the constructor
        self.assertEqual(len(self.client1._accounts), 1)

        # Test assert for trying to close an account with the number not being an int
        try:
            result = self.client1.closeAccount("Invalid")
        except AssertionError:
            print("Test Passed: Object not created")

        # Test assert for trying to close an account with the number being less than 1000
        try:
            result = self.client1.closeAccount(10)
        except AssertionError:
            print("Test Passed: Object not created")

        # Attempt to close a nonexistant account, should return False
        result = self.client1.closeAccount(9999)
        self.assertEqual(result, False)

        #Adding a 2nd account so we can close it with no balance
        self.client1.openAccount("c")
        self.assertEqual(len(self.client._accounts), 2)

        #Closing 2nd account with a balance of zero, should return True
        result = self.client1.closeAccount(self.client1._accounts[1].getAccountNumber())
        self.assertEqual(result, True)
        self.assertEqual(len(self.client1._accounts),1)

        #Adding an account so we can close it with a positive balance
        self.client1.openAccount("c")
        self.assertEqual(len(self.client._accounts), 2)
        self.client1.accounts[1].deposit(1000.0)

        #Closing the account with a positive balance, should return True
        result = self.client1.closeAccount(self.client1._accounts[1].getAccountNumber())
        self.assertEqual(result, True)
        self.assertEqual(len(self.client1._accounts),1)

        #Adding an account so we can close it with a negative balance
        self.client1.openAccount("c")
        self.assertEqual(len(self.client._accounts), 2)
        # Cannot deposit negative values, so a transaction is appended 
        self.client1.accounts[1]._transactions.append(Transaction(100,'withdrawal',-100.0))

        #Closing the account with a negative balance, should return False
        result = self.client1.closeAccount(self.client1._accounts[1].getAccountNumber())
        self.assertEqual(result, False)
        self.assertEqual(len(self.client1._accounts),2)
        
    def test_print_client(self):
        pass

if __name__ == "__main__":
    unittest.main()
