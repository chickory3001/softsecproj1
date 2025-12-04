# LastNameTester.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 3
# 
# Import the unittest module and the LastName class.
# Test each method of LastName to get full branch coverage.
# Note: When using coverage report, it will show the DEBUG statements as failing.

import unittest
from LastName import LastName

class TestLastName(unittest.TestCase):

  validLast1 = "Davidson"
  validLast2 = "Skyler"
  invalidLast = "Davidsonnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
  
  DEBUG = True

  def setUp(self):
      self.LastName1 = LastName(self.validLast1)
      self.LastName2 = LastName(self.validLast2)

  def test_constructor(self):
    if self.DEBUG:
      print("\nTesting the constructor")
    
    self.assertEqual(self.LastName1._name, TestLastName.validLast1)
    self.assertEqual(self.LastName2._name, TestLastName.validLast2)
    
  def test_constructor_asserts(self):
    if self.DEBUG:
      print("\nTesting the constructor asserts")
    
    with self.assertRaises(AssertionError):
      LastName(self.invalidLast)

if __name__ == "__main__":
    unittest.main()
