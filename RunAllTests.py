#simple program to import all the test classes and run them
import unittest
from TestTransaction import TestTransaction
from CheckingAccountTester import TestCheckingAccount
from SavingsAccountTester import TestSavingsAccount
from ClientTester import TestClient
from AddressTester import TestAddress

if __name__ == '__main__':
    suppressPrintStatements = True
    unittest.main(buffer=suppressPrintStatements)