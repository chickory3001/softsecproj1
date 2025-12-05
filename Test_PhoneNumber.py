# FirstNameTester.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 3
# 
# Import the unittest module and the FirstName class.
# Test each method of both FirstName and Name to get full branch coverage.
# Note: When using coverage report, it will show the DEBUG statements as failing.

import unittest
from PhoneNumber import PhoneNumber

class TestPhoneNumber(unittest.TestCase):

  VALIDPHONE = '9123456789'
  ALSO_VALID = "912-345-6789"
  DEBUG = True

  def setUp(self):
    self.phonenum = PhoneNumber(TestPhoneNumber.VALIDPHONE)
    self.phone2 = PhoneNumber(TestPhoneNumber.ALSO_VALID)

  def test_constructor(self):
    if self.DEBUG:
      print("\nTesting the constructor")
    
    self.assertEqual(self.phonenum.getPhoneNum(), TestPhoneNumber.VALIDPHONE)
    self.assertEqual(self.phone2.getPhoneNum(), TestPhoneNumber.VALIDPHONE)
  
  def test_constructor_asserts(self):
    pass
  
  

if __name__ == "__main__":
  unittest.main()
