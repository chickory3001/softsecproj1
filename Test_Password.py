"""
Testing the password class

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
Import the password and client class
"""
from Password import password
from Client import Client


#Created a list of passwords to test, valid tests and invalid test
class passwordTester(self):
  def __init__(self):
    self._validPassword = ["randyBoBandy84", "Alpha2025", "CodingKing88", "SecurePass12", "NightWolf77"]
    self._invalidPassword = ["linesAmIRight?||||", "Bad/Pass1", "Wrong\\Key9", "Too<Short", "Space Bar1"] 
    self.passwordObj = Password()  #creating a password object to test

  #Testing valid passwords from list
  def testValidPass(self):
    print("Testing valid passwords:")
    for passwords in self.validPasswords:
      result = self.passwordObj.isValid(passwords)
      print(f" {passwords}: {"FAIL (correct)" if not result else "PASS (should NOT be valid!)"}")
  
  #Testing invalid passwords form list
  def testInvalidPass(self):
    print("Testing invalid passwords:")
    for passwords in self.invalidPasswords:
      result = self.passwordObj.isValid(passwords)
      print(f"  {passwords}: {'FAIL (correct)' if not result else 'PASS (should NOT be valid!)'}")

  def testChangingPassword(self):
    print("Testing password changes")
    oldPass = self._validPassword[0]
    newPass = "ValidNewPass67"

    self.passwordObj._password = oldPass
    changeResult = self.passwordObj.changePassword(oldPass, newPass)
    print(f" Changing VALID -> VALID: {oldPass} -> {newPass}: {'SUCCESS' if changeResult else 'FAIL'}")

    oldInvalid = self._invalidPassword[0]
    newInvalid = "invalidNewPass|||67"

    self.passwordObj._password = oldInvalid
    changeResult = self.passwordObj.changePassword(oldInvalid, newInvalid)
    print(f" Changing INVALID -> INVALID: {oldInvalid} -> {newInvalid}: {SUCCESS (should NOT happen!}' if changeResult else 'FAIL (correct)'}")


    

if __name__ == "__main__":
  tester = PasswordTester()
  tester.test_validPassword()
  tester.test_invalidPasswords()




  
