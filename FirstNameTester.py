"""
Unit Test using Python's unittest module and assertions

Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett

Import the unittest module and the FirstName module.
Test each method for full branch coverage
"""

import unittest
from FirstName import FirstName

class TestFirstName(unittest.TestCase):

  validFirst1 = "David"
  validFirst2 = "Skyler"
  invalidName1 = 5
  invalidName2 = "David\n"
  invalidName3 = ""
  invalidFirst = "Davidddddddddddddddddddddd"

  debug = False


  def setUp(self):
    self.FirstName1 = FirstName(validFirst1)
    self.FirstName2 = FirstName(validFirst2)

  def test_constructor(self):
    if TestCheckingAccount.DEBUG:
      print("\nTesting the constructor")
    
    self.assertEqual(self.FirstName1.getName(), TestFirstName.validFirst1)
    self.assertEqual(self.FirstName2.getName(), TestFirstName.validFirst2)
    self.assertTrue(isinstance(self.FirstName1, str))
    self.assertTrue(isinstance(self.FirstName2, str))
    
  def test_constructor_asserts(self):
    if TestCheckingAccount.DEBUG:
      print("\nTesting the constructor asserts")
    
    with self.assertRaises(AssertionError):
      FirstName(invalidName1)
    with self.assertRaises(AssertionError):
      FirstName(invalidName2)
    with self.assertRaises(AssertionError):
      FirstName(invalidName3)
    with self.assertRaises(AssertionError):
      FirstName(invalidFirst)
    
  def test_getName(self):
    if TestCheckingAccount.DEBUG:
      print("\nTesting the getter method")

    self.assertEqual(self.FirstName1.getName(), TestFirstName.validFirst1)

    
  def test_eq(self):
    if TestCheckingAccount.DEBUG:
      print("\nTesting the equal special method")
      
    self.assertTrue(self.FirstName1 == self.FirstName1)
    self.assertFalse(self.FirstName1 == self.FirstName2)
    
  def test_lt(self):
    if TestCheckingAccount.DEBUG:
      print("\nTesting the less than special method")
            
    self.assertTrue(self.FirstName1 < self.FirstName2)
    self.assertFalse(self.FirstName1 < self.FirstName1)
    
  def test_le(self):
    if TestCheckingAccount.DEBUG:
      print("\nTesting the less than or equal to special method")
            
    self.assertTrue(self.FirstName1 <= self.FirstName1)
    self.assertTrue(self.FirstName1 <= self.FirstName2)
    self.assertFalse(self.FirstName2 <= self.FirstName1)
