"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the Address module.
Test each method with at least one unit test.
"""

import unittest
from Address import Address

class TestAddress(unittest.TestCase):
    
    # Inconsistent cases will be corrected by the Address class
    STREET_ = '304 timmy Drive'
    CITY_ = 'Glen alLen'
    STATE_ = 'vA'
    
    # The correct output for what Address should spit out
    STREET = "304 Timmy Drive"
    CITY = "Glen Allen"
    STATE = "VA"
    
    DEBUG = True
    
    # setUp creates an address
    def setUp(self):   
        self.address1 = Address(TestAddress.STREET_,
                                TestAddress.CITY_,
                                TestAddress.STATE_
                                )
    
    # Tests constructor
    def test_constructor(self):
        if TestAddress.DEBUG:
            print('\nTesting constructor')
        
        self.assertEqual(self.address1._street, TestAddress.STREET)
        self.assertEqual(self.address1._city, TestAddress.CITY)
        self.assertEqual(self.address1._state, TestAddress.STATE)

    # Tests constructor assertions 
    def test_constructor_asserts(self):
        if TestAddress.DEBUG:
            print('\nTesting constructor asserts')
        
        # Test string type assert
        with self.assertRaises(AssertionError):
            Address(1, TestAddress.CITY, TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET, 1, TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET, TestAddress.CITY, 1)
        
        # Test alphanumeric assert 
        with self.assertRaises(AssertionError):
            Address(' @#$%^', TestAddress.CITY, TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET, ' @#$%^', TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET, TestAddress.CITY, ' @#$%^')
        
        # Test length assert
        with self.assertRaises(AssertionError):
            Address('', TestAddress.CITY, TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address('a'*31, TestAddress.CITY, TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET, '', TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET, 'a'*31, TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET, TestAddress.CITY, 'aaaa')
        
        # Test in list of states assert
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET, TestAddress.CITY, 'ZZ')
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET, TestAddress.CITY, 'vaa') 
            
    # Tests getStreet method
    def test_getStreet(self):
        if TestAddress.DEBUG:
            print("\nTesting getStreet method")
            
        self.assertEqual(self.address1.getStreet(), TestAddress.STREET)
        
    # Tests getCity method
    def test_getCity(self):
        if TestAddress.DEBUG:
            print("\nTesting getCity method")
            
        self.assertEqual(self.address1.getCity(), TestAddress.CITY)
        
    # Tests getState method
    def test_getState(self):
        if TestAddress.DEBUG:
            print("\nTesting getState method")
            
        self.assertEqual(self.address1.getState(), TestAddress.STATE)

if __name__ == "__main__":
    unittest.main()
