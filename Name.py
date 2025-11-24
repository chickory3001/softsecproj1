# Name.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 2
# 
# This module defines the FirstName class.
# Holds a single string with restrictions on its structure

class Name:

  # Construct the Name object
  # @param first: the first name as a string
  # @require first is a str of length 1-25 with no special characters
  def __init__(self, name: str) -> 'name':
    assert isInstance(name, str)
    assert name.isPrintable()
    assert 1 <= len(name)
      
