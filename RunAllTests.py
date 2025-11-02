#simple program to import all the test classes and run them
import unittest
from TestTransaction import TestTransaction
from CheckingAccountTester import TestCheckingAccount
from AddressTester import TestAddress

if __name__ == '__main__':
    unittest.main()