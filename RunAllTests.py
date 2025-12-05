# Simple program to import all the test classes and run them

import unittest
from TestTransaction import TestTransaction
from Test_CheckingAccount import TestCheckingAccount
from Test_SavingsAccount import TestSavingsAccount
from Test_Client import TestClient
from Test_Address import TestAddress
from Test_Encryption import TestEncryption
from Test_FirstName import TestFirstName
from Test_LastName import TestLastName
from Test_PasswordAndHashedPWD import passwordTester

if __name__ == '__main__':
    suppressPrintStatements = True
    unittest.main(buffer=suppressPrintStatements)
