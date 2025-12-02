# FirstName.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 3
# 
# This module defines the FirstName class.
# Holds a single string with restrictions on its structure

from Name import Name

class FirstName(Name):

  def __init__(self, name: str) -> 'firstName':
    super().__init__(name)
    assert len(name) <= 25

