# Client.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 2
# This is the tester for the client 

import unittest
from Address import Address
from Client import Client


class ClientTester:
#Testers
  firstNames = ["Reggie", "Homer", "Jeff", "Matt", "Ryan"]
  lastNames = ["Sonic", "Randall", "Arin", "Dan", "Adam"]
  phoneNumbers = ["3456789012", "4567890123", "5678901234", "6789012345", "7890123456"]
  address = Address("CaryStreet", "Richmond", "Va")
  
  def testNames(self):
    for i in range(len(self.firstNames)):
      c = Client(self.firstNames[i], self.lastNames[i], self.assertEqual(c.getFirstName(), self.firstName[i]), self.assertEqual(c.getLastName(), self.lastNames[i])self.assertEqual(len(c._accounts),1)
  #---------------------------------------------------------------------------------------------------------------
  #currently working on this, I don't come home until 10pm today, it will be done. Just don't touch please. -Josh
  #---------------------------------------------------------------------------------------------------------------
  
    
    
    
