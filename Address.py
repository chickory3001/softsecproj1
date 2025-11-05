# Address.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 2
# 
# This module defines the Address class.
# A simple class to hold 3 string parts of an address. 

class Address:
    #constructs an address object
    #@param street: the street of the client address 
    #@param city: the city of the client address 
    #@param state: the state of the client address 
    #@require street is a str of length 1-30 with no special characters
    #@require city is a str of length 1-30 with no special characters
    #@require state is a str of length 2 with no special characters, must be one of VA, MD, NJ, PA, DE, NC, WV, DC
    def __init__(self, street: str, city: str, state: str) -> 'Address':
        assert isinstance(street, str) and 1 <= len(street) <= 30, 'invalid street'
        assert isinstance(city, str) and 1 <= len(city) <= 30, 'invalid city'
        assert isinstance(state, str) and state.isalpha() and len(state) == 2 and state.upper() in ["VA", 'MD', 'NJ', 'PA', 'DE', 'NC', 'WV', 'DC'], 'invalid state'
        
        # Verify valid street name (allowing for spaces and numbers)
        splitStreet = street.split()
        for s in splitStreet:
            assert s.isalnum(), "invalid street name"
        
        # Verify valid city name (allowing for spaces in city name)
        splitCity = city.split()
        for c in splitCity:
            assert c.isalpha(), "invalid city name"
        
        self._street = street.title()
        self._city = city.title()
        self._state = state.upper()
    
    # Returns a string containing the formatted address.
    # @return: The formatted string of the address
    def __str__(self) -> str:
        return f'{self._street}\n{self._city}, {self._state}'
