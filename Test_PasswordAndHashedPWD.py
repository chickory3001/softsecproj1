"""
Testing the password class

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
Import the password and client class
"""
from Password import Password
from Client import Client
import unittest
from HashedPWD import HashedPWD

#Created a list of passwords to test, valid tests and invalid test
class passwordTester(unittest.TestCase):
  validPasswords = ["randyBoBandy84", "Alpha2025", "CodingKing88", "SecurePass12", "NightWolf77"]
  invalidPasswords = ["lines||||||", "Bad/Pass1", '>>>>>>>>>>', "Wrong\\Key9", 'space bar', "2Short",'<<<<<<<<<<','toolongggggggggggggggggg',b'wrongtype'] 
  

  def setUp(self):
    self.password = Password("randyBoBandy84")  #creating a password object to test
    self.hashedpwd = HashedPWD(self.password)
  
  #Testing valid passwords from list
  #@Require that the passwords are correctly entered
  #@Ensure the passwords do return true 
  def testValidPass(self):
    print("Testing valid passwords:")
    for password in passwordTester.validPasswords:
      # creates different test for each value, so if multiple fail it will show 
      with self.subTest(password=password):
        result = Password.passwordChecker(password)
        self.assertTrue(result)
  
  #Testing invalid passwords form list
  #@Require that the passwords are correctly entered
  #@Ensure the passwords do return false
  def testInvalidPass(self):
    print("Testing invalid passwords:")
    for password in self.invalidPasswords:
      # creates different test for each value, so if multiple fail it will show 
      with self.subTest(password=password):
        result = Password.passwordChecker(password)
        self.assertFalse(result)

  #test constructor 
  def test_constructors(self):
    self.assertEqual(Password("randyBoBandy84").getPassword(), "randyBoBandy84")
    self.assertEqual(HashedPWD(Password("randyBoBandy84")).getHash(), HashedPWD(Password("randyBoBandy84"))._hashPWD)
  
  #test constructor asserts:
  def test_constructor_asserts(self):
    for password in self.invalidPasswords:
      # creates different test for each value, so if multiple fail it will show 
      with self.subTest(password=password):
        with self.assertRaises(AssertionError):
          Password(password)
  
  # test assertions
  def test_hashedpwd_asserts(self):
    with self.assertRaises(AssertionError):
      HashedPWD(self.password,'jfkds;lafjdksal;')
    with self.assertRaises(AssertionError):
      HashedPWD('jkl;fdsa')
    with self.assertRaises(AssertionError):
      HashedPWD(self.password,pepper=12313)
    
    with self.assertRaises(AssertionError):
      self.hashedpwd._createSecureHash(123)
    with self.assertRaises(AssertionError):
      self.hashedpwd._checkPassword(123)
    with self.assertRaises(AssertionError):
      self.hashedpwd == 123
  
  #test repr, to be manually verified
  def test_repr(self):
    print(repr(self.hashedpwd))


if __name__ == "__main__":
  unittest.main()
