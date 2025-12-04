# FirstNameTester.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 3
# 
# Import the unittest module and the FirstName class.
# Test each method of both FirstName and Name to get full branch coverage.
# Note: When using coverage report, it will show the debug statements as failing.

import unittest
from FirstName import FirstName

class TestFirstName(unittest.TestCase):

  validFirst1 = "David"
  validFirst2 = "Skyler"
  invalidName1 = 5
  invalidName2 = "David\n"
  invalidName3 = ""
  invalidFirst = "Davidddddddddddddddddddddd"

  debug = True


  def setUp(self):
    self.FirstName1 = FirstName(self.validFirst1)
    self.FirstName2 = FirstName(self.validFirst2)

  def test_constructor(self):
    if self.debug:
      print("\nTesting the constructor")
    
    self.assertEqual(self.FirstName1._name, TestFirstName.validFirst1)
    self.assertEqual(self.FirstName2._name, TestFirstName.validFirst2)
    
  def test_constructor_asserts(self):
    if self.debug:
      print("\nTesting the constructor asserts")
    
    with self.assertRaises(AssertionError):
      FirstName(self.invalidName1)
    with self.assertRaises(AssertionError):
      FirstName(self.invalidName2)
    with self.assertRaises(AssertionError):
      FirstName(self.invalidName3)
    with self.assertRaises(AssertionError):
      FirstName(self.invalidFirst)
    
  def test_getName(self):
    if self.debug:
      print("\nTesting the getter method")

    self.assertEqual(self.FirstName1.getName(), TestFirstName.validFirst1)

    
  def test_eq(self):
    if self.debug:
      print("\nTesting the equal special method")
      
    self.assertTrue(self.FirstName1 == self.FirstName1)
    self.assertFalse(self.FirstName1 == self.FirstName2)
    
  def test_lt(self):
    if self.debug:
      print("\nTesting the less than special method")
            
    self.assertTrue(self.FirstName1 < self.FirstName2)
    self.assertFalse(self.FirstName1 < self.FirstName1)
    
  def test_le(self):
    if self.debug:
      print("\nTesting the less than or equal to special method")
            
    self.assertTrue(self.FirstName1 <= self.FirstName1)
    self.assertTrue(self.FirstName1 <= self.FirstName2)
    self.assertFalse(self.FirstName2 <= self.FirstName1)
