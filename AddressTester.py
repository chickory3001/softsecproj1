"""
Simple Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the BankAccount module.
Test each method with at least one unit test.
"""

import unittest
from BankAccount import BankAccount
"""Define TestBankAccount class by extending the unittest.TestCase class"""

class TestAddress(unittest.TestCase):
    def setUp(self):
        # print('setup')
        self.bankAccount1 = BankAccount("Tim", "Apple")
        self.bankAccount2 = BankAccount("Billiam", "Gates")