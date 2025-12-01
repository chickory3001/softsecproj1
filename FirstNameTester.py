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
    self.assertEqual(self.FirstName1.getName(), TestFirstName.validFirst1)
    self.assertEqual(self.FirstName2.getName(), TestFirstName.validFirst2)
    self.assertTrue(isinstance(self.FirstName1, str))
    self.assertTrue(isinstance(self.FirstName2, str))
    
  def test_constructor_asserts(self):

    
  def test_getName(self):
  def test_eq(self):
  def test_lt(self):
  def test_le(self):
