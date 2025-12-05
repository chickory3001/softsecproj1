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
  invalidPasswords = ["linesAmIRight?||||", "Bad/Pass1", "Wrong\\Key9", "Too<Short"] 
  

  def setUp(self):
    self.passwordObj = Password("randyBoBandy84")  #creating a password object to test
  
  
  #Testing valid passwords from list
  #@Require that the passwords are correctly entered
  #@Ensure the passwords do return true 
  def testValidPass(self):
    print("Testing valid passwords:")
    for password in passwordTester.validPasswords:
      # creates different test for each value, so if multiple fail it will show 
      with self.subTest(password=password):
        result = self.passwordObj.passwordChecker(password)
        self.assertTrue(result)
  
  #Testing invalid passwords form list
  #@Require that the passwords are correctly entered
  #@Ensure the passwords do return false
  def testInvalidPass(self):
    print("Testing invalid passwords:")
    for password in self.invalidPasswords:
      # creates different test for each value, so if multiple fail it will show 
      with self.subTest(password=password):
        result = self.passwordObj.passwordChecker(password)
        self.assertFalse(result)

  #test constructor 
  def test_constructor(self):
    self.assertEqual(Password("randyBoBandy84")._password, "randyBoBandy84")
  
  #test constructor asserts:
  def test_constructor_asserts
  
  
  #Testing changing of passwords from both valid and invalid
  #@Require that the passwords are correctly entered
  #@Ensure the passwords do return true if valid and false if not
  # def testChangingPassword(self):
  #   print("Testing password changes")
    
  #   #Testing valid password change
  #   oldPass = self._validPassword[0]
  #   newPass = "ValidNewPass67"

  #   self.passwordObj._password = oldPass     #Making password object to store previous passwords 
  #   changeResult = self.passwordObj.changePassword(oldPass, newPass)
  #   print(f" Changing VALID -> VALID: {oldPass} -> {newPass}: {'SUCCESS' if changeResult else 'FAIL'}")

    
  #   #Testing invalid password change
  #   oldInvalid = self._invalidPassword[0]
  #   newInvalid = "invalidNewPass|||67"

  #   self.passwordObj._password = oldInvalid    #Making password object to store previous passwords 
  #   changeResult = self.passwordObj.changePassword(oldInvalid, newInvalid)
  #   print(f" Changing INVALID -> INVALID: {oldInvalid} -> {newInvalid}: {SUCCESS (should NOT happen!}' if changeResult else 'FAIL (correct)'}")


    

if __name__ == "__main__":
  unittest.main()
