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
    PHONE= 9123456789
    ADDRESS = Address('timmydrive','glenallen','VA')
    DEBUG = False

    # The setup method craetes a client
    def setUp(self):
        self.client1 = Client('timmy','smith',9123456789,Address('timmydrive','glenallen','VA'), 'checking')

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
        self.assertEqual(self.client1._nextClientNumber, 1001)
        self.assertEqual(self.client1.openAccount, 'checking')
        
    def test_client_checking(self):
        Client('timmy','smith',9123456789,Address('timmydrive','glenallen','VA'), 'checking')
        self.assertEqual(client._accountType.lower(), 'checking')

    def test_client_savings(self):
        Client('timmy','smith',9123456789,Address('timmydrive','glenallen','VA'), 'savings')
        self.assertEqual(client._accountType.lower(), 'savings')

    def test_first_name(self):
        with self.assertRaises(AssertionError):
            Client("t1mmy", "smith", 9123456789, TestClient.ADDRESS, "Checking")
            
    def test_last_name(self):
        with self.assertRaises(AssertionError):
            Client("timmy", "sm1th", 9123456789, TestClient.ADDRESS, "Checking")
            
    def test_phone_length(self):
        with self.assertRaises(AssertionError):
            Client("timmy", "smith", 912345678, TestClient.ADDRESS, "Checking")
            
    def test_phone_start_digit(self):
        with self.assertRaises(AssertionError):
            Client("timmy", "smith", 2123456789, TestClient.ADDRESS, "Checking") 
            
    def test_address(self):
        with self.assertRaises(AssertionError):
            Client("timmy", "Brown", 9123456789, "Address", "Checking")
            
    def test_set_first_name(self):
        client = Client("timmy", "smith", 9123456789, TestClient.ADDRESS, "Checking")
        with self.assertRaises(AssertionError):
                    client._setFirstName("t1mmy")
                    
    def test_set_last_name(self):
        client = Client("timmy", "smith", 9123456789, TestClient.ADDRESS, "Checking")
        with self.assertRaises(AssertionError):
                    client._setLastName("sm1th") 
                    
    def test_open_account(self):
        Client('timmy','smith',9123456789,Address('timmydrive','glenallen','VA'), 'checking')
        result = client.openAccount('checking')
        self.assertTrue('checking' in client._accounts)
        self.assertEqual(result, "Savings account opened successfully")
        
    def test_close_account(self):
        Client('timmy','smith',9123456789,Address('timmydrive','glenallen','VA'), 'checking')
        client.openAccount('checking')
        result = client.closeAccount('checking')
        self.assertTrue('checking' not in client._accounts)
        self.assertEqual(result, "Savings account closed successfully")
        
    def test_print_client(self):
        pass