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
  DEBUG = True

  def setUp(self):
    self.phonenum = PhoneNumber(TestPhoneNumber.VALIDPHONE)

  def test_constructor(self):
    if self.DEBUG:
      print("\nTesting the constructor")
    
    self.assertEqual(self.phonenum.getPhoneNum(), TestPhoneNumber.VALIDPHONE)
  
  def test_constructor_asserts(self):


if __name__ == "__main__":
    unittest.main()