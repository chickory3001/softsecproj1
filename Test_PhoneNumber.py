# Test_PhoneNumber.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 3
# 
# Import the unittest module and the PhoneNumber class.
# Note: When using coverage report, it will show the DEBUG statements as failing.

import unittest
from PhoneNumber import PhoneNumber

class TestPhoneNumber(unittest.TestCase):

  VALIDPHONE = '9123456789'
  ALSO_VALID = "912-345-6789"
  INVALID_TYPE: int = 912_345_6789
  INVALID_LEN = "91234567899"
  INV_0 = "0123456789"
  INV_1 = "1123456789"
  INV_2 = "2123456789"
  INV_HYPH_0 = "912345-6789"
  INV_HYPH_1 = "912-3-45-6789"
  INV_HYPH_2 = "912-3-5-6789"
  ALPHANUM = "912-346-578a"
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
    if self.DEBUG:
      print("\nTesting the constructor asserts")
    
    # Test invalid type.
    with self.assertRaises(AssertionError):
      inv = PhoneNumber(TestPhoneNumber.INVALID_TYPE)
    
    # Test invalid length.
    with self.assertRaises(AssertionError):
      inv = PhoneNumber(TestPhoneNumber.INVALID_LEN)
    
    # Test invalid beginning number.
    with self.assertRaises(AssertionError):
      inv = PhoneNumber(TestPhoneNumber.INV_0)
    with self.assertRaises(AssertionError):
      inv = PhoneNumber(TestPhoneNumber.INV_1)
    with self.assertRaises(AssertionError):
      inv = PhoneNumber(TestPhoneNumber.INV_2)
    
    # Test invalid hyphen use.
    with self.assertRaises(AssertionError):
      inv = PhoneNumber(TestPhoneNumber.INV_HYPH_0)
    with self.assertRaises(AssertionError):
      inv = PhoneNumber(TestPhoneNumber.INV_HYPH_1)
    with self.assertRaises(AssertionError):
      inv = PhoneNumber(TestPhoneNumber.INV_HYPH_2)
      
    # Test invalid character.
    with self.assertRaises(AssertionError):
      inv = PhoneNumber(TestPhoneNumber.ALPHANUM)

if __name__ == "__main__":
  unittest.main()
