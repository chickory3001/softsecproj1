"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the Address module.
Test each method with at least one unit test.
"""

import unittest
from Address import Address

class TestAddress(unittest.TestCase):
    STREET = 'Timmy Drive'
    CITY = 'Glen Allen'
    STATE = 'VA'
    DEBUG = False
    #setup creates an address
    def setUp(self):
        # print('setup')
        self.address1 = Address(TestAddress.STREET,TestAddress.CITY,TestAddress.STATE)
    
    #tests constructor
    def test_constructor(self):
        if TestAddress.DEBUG:
            print('\n testing constructor')
        self.assertEqual(self.address1._street,TestAddress.STREET)
        self.assertEqual(self.address1._city,TestAddress.CITY)
        self.assertEqual(self.address1._state,TestAddress.STATE)

    #tests constructor assertions 
    def test_constructor_asserts(self):
        if TestAddress.DEBUG:
            print('\n testing constructor asserts')
        
        #test string type assert
        with self.assertRaises(AssertionError):
            Address(1,TestAddress.CITY,TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET,1,TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET,TestAddress.CITY,1)
        
        #test alphanumeric assert 
        with self.assertRaises(AssertionError):
            Address(' @#$%^',TestAddress.CITY,TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET,' @#$%^',TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET,TestAddress.CITY,' @#$%^')
        
        #test length assert
        with self.assertRaises(AssertionError):
            Address('',TestAddress.CITY,TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address('a'*31,TestAddress.CITY,TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET,'',TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET,'a'*31,TestAddress.STATE)
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET,TestAddress.CITY,'aaaa')
        
        # test in list of states assert
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET,TestAddress.CITY,'ZZ')
        with self.assertRaises(AssertionError):
            Address(TestAddress.STREET,TestAddress.CITY,'va') 

if __name__ == "__main__":
    unittest.main()
