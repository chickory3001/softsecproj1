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

    self._name = name

  ### QUERIES ###

  # getName returns the name
  # @return self._name: the name as a string
  def getName(self) -> str:
    return self._name

  ### SPECIAL METHODS ###
    
  # Tests quality between two names
  # @ensure self is being compared to another Name
  # @return: True if equal, else False
  def __eq__(self, other: 'Name') -> bool:
    assert isInstance(other, Name), "Invalid comparison"
    return self._name == other._name

  # Tests less than comparison between two names
  # @ensure self is being compared to another Name
  # @return: True if equal, else False
  def __lt__(self, other: 'Name') -> bool:
    assert isInstance(other, Name), "Invalid comparison"
    return self._name < other._name

  # Tests less than or equal to comparison between two names
  # @ensure self is being compared to another Name
  # @return: True if equal, else False
  def __le__(self, other: 'Name') -> bool:
    assert isInstance(other, Name), "Invalid comparison"
    return self._name <= other._name

