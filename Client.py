# Client.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 2
# 
# This module defines the Client class.
# A class to represent a client in a banking software.

from BankAccount import *
from Address import Address

class Client:
    # client numbers start at 100 
    _nextClientNumber = 100

    #creates a client object 
    #@param first: the first name as a string
    #@param last: the last name as a string 
    #@param phone: the phone number of the client
    #@param street: the street of the client address 
    #@param city: the city of the client address 
    #@param state: the state of the client address 
    #@require first is a str of length 1-25 with no special characters
    #@require last is a str of length 1-40 with no special characters
    #@require phone is all digits, length of 10, doesn't start with 0, 1, or 2
    #@require street is a str of length 1-30 with no special characters
    #@require city is a str of length 1-30 with no special characters
    #@require state is a str of length 2 with no special characters, must be one of VA, MD, NJ, PA, DE, NC, WV, DC
    def __init__(self, first: str, last: str, phone: int, street: str, city: str, state: str):
        assert isinstance(first, str) and first.isalpha() and 1 <= len(first) <= 25, 'invalid first name'
        assert isinstance(last, str) and last.isalpha() and 1 <= len(last) <= 40, 'invalid last name'
        #attempt to cast phone num to int, throw assertion error if it fails. 
        #this way it accepts strings, floats, and ints so long as it's castable to int  
        try:
            phone = int(phone)
        except:
            assert False, 'invalid phone number'
        phonestr = str(phone)
        assert len(phonestr) == 10 and not phonestr[0] in ['0','1','2'] and phonestr.isalpha(), 'invalid phone number'
        assert isinstance(street, str) and street.isalpha() and 1 <= len(street) <= 30, 'invalid street'
        assert isinstance(city, str) and city.isalpha() and 1 <= len(city) <= 30, 'invalid city'
        assert isinstance(state, str) and state.isalpha() and len(state) == 2 and state in ["VA", 'MD', 'NJ', 'PA', 'DE', 'NC', 'WV', 'DC'], 'invalid state'
        
        self._first = first
        self._last = last
        self._phone = phone
        self._address = Address(street,city,state)
        self._accounts = []
        self._clientNumber = Client._nextClientNumber
        #increment the next client number 
        Client._nextClientNumber += 1
    
    
    #updates the first name of the client
    #@param first: new first name string 
    #@require first is a str of length 1-25 with no special characters
    def _setFirstName(self,first:str):
        assert 1 <= len(first) <= 25 and first.isalpha and isinstance(first, str), 'invalid first name'
        self._first = first
    
    #updates the last name of the client
    #@param last: new last name string 
    #@require last is a str of length 1-40 with no special characters
    def _setLastName(self,last:'str'):
        assert 1 <= len(last) <= 25 and last.isalpha and isinstance(last, str), 'invalid last name'
        self._last = last

if __name__ == "__main__":
    client = Client('timmy','smith',1,'feafe','feafea','efafea')
    print(client._address._street)
