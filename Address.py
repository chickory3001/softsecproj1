# Address.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 2
# 
# This module defines the Address class.
# A simple class to hold 3 string parts of an address. 

class Address:
    def __init__(self, street: str, city: str, state: str):
        self._street = street
        self._city = city
        self._state = state