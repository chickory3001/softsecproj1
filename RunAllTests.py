# Simple program to import all the test classes and run them

import unittest
from TestTransaction import TestTransaction
from Test_CheckingAccount import TestCheckingAccount
from SavingsAccountTester import TestSavingsAccount
from Test_Client import TestClient
from Test_Address import TestAddress
from EncryptionTester import TestEncryption

if __name__ == '__main__':
    suppressPrintStatements = True
    unittest.main(buffer=suppressPrintStatements)
