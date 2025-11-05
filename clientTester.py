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
    ADDRESS = Address('timmydrive','glenallen','VA')
    DEBUG = False

    # The setup method craetes a client
    def setUp(self):
        self.client1 = Client('timmy','smith',TestClient.Phone,TestClient.Address, 'Checking')

    #Tests constuctor   
    def test_constructor(self):
        if TestClient.DEBUG:
            print("\nTesting the constructor")
            print("The first client: ", self.client1)
            
        self.assertEqual(self.client1.getFirstName(), TestClient.FIRSTNAME)
        self.assertEqual(self.client1.getLastName(), TestClient.LASTNAME)
        self.assertEqual(self.client1._phone, TestClient.PHONE)
        self.assertEqual(self.client1.Address, TestClient.ADDRESS)
        self.assertEqual(self.client1._clientNumber, 1000)

        
    def test_client_checking(self):
        client = Client('timmy','smith',9123456789,Address('timmydrive','glenallen','VA'), 'checking')
        self.assertEqual(client._accountType.lower(), 'checking')

    def test_client_savings(self):
        client = Client('timmy','smith',9123456789,Address('timmydrive','glenallen','VA'), 'savings')
        self.assertEqual(client._accountType.lower(), 'savings')
     
    # Testing an invalid first name
    def test_first_name(self):
        with self.assertRaises(AssertionError):
            Client("t1mmy", "smith", 9123456789, TestClient.ADDRESS, "Checking")
    # Testing an invalid last name         
    def test_last_name(self):
        with self.assertRaises(AssertionError):
            Client("timmy", "sm1th", 9123456789, TestClient.ADDRESS, "Checking")
    
    # Testing an invalid phone length        
    def test_phone_length(self):
        with self.assertRaises(AssertionError):
            Client("timmy", "smith", 912345678, TestClient.ADDRESS, "Checking")
    
    # Testing an invalid staring digit for phone number        
    def test_phone_start_digit(self):
        with self.assertRaises(AssertionError):
            Client("timmy", "smith", 2123456789, TestClient.ADDRESS, "Checking") 
    # Testing an invalid adress        
    def test_address(self):
        with self.assertRaises(AssertionError):
            Client("timmy", "Brown", 9123456789, "Address", "Checking")
    
    # Tests setting an invalid first name        
    def test_set_first_name(self):
        client = Client("timmy", "smith", 9123456789, TestClient.ADDRESS, "Checking")
        with self.assertRaises(AssertionError):
                    client._setFirstName("t1mmy")
    # Tests setting an invalid last name              
    def test_set_last_name(self):
        client = Client("timmy", "smith", 9123456789, TestClient.ADDRESS, "Checking")
        with self.assertRaises(AssertionError):
                    client._setLastName("sm1th") 
    # Testing opening an account               
    def test_open_account(self):
        if TestClient.DEBUG:
            print("\nTesting the openAccount method")
            
        #Testing a valid checking account opening
        self.client1.openAccount("c")
        self.assertEqual(len(self.client1._accounts), 1)
        self.assertEqual(self.client1._accounts[0].accountType, "Checking")

        #Testing a valid checking account opening
        self.client1.openAccount("s")
        self.assertEqual(len(self.client1._accounts), 2)
        self.assertEqual(self.client1._accounts[1].accountType, "Savings")

        #Testing that having the type argument not be of type string leads to assert error
        try:
            result = self.client1.openAccount(10)
        except AssertionError:
            print("Test Passed: Object not created")
        self.assertEqual(len(self.client1._accounts), 2)
        
        #Testing that having the type argument not be either "c" or "s" leads to assert error
        try:
            result = self.client1.openAccount("Invalid")
        except AssertionError:
            print("Test Passed: Object not created")
        self.assertEqual(len(self.client1._accounts), 2)
    
    # Testing closing an account   
    def test_close_account(self):
        if TestClient.DEBUG:
            print("\nTesting the closeAccount method")
        #1 is the checking account created from the constructor
        self.assertEqual(len(self.client._accounts), 1)

        #Adding a 2nd account so we can close it
        self.client1.openAccount("Checking")
        self.assertEqual(len(self.client._accounts), 2)

        #Closing 2nd account
        self.client1.closeAccount(self.client1._accounts[1].getAccountNumber())
        self.assertEqual(len(self.client1._accounts),1)

        #Closing a non existent account, should do nothing
        result = self.client1.closeAccount(9999)
        self.assertIsNone(result)
        self.assertEqual(len(self.client1._accounts),1)
        
    def test_print_client(self):
        pass
