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
from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

class Client:
    # client numbers start at 100 
    _nextClientNumber = 100

    #creates a client object 
    #@param first: the first name as a string
    #@param last: the last name as a string 
    #@param phone: the phone number of the client
    #@param address: the address of the client 
    #@require first is a str of length 1-25 with no special characters
    #@require last is a str of length 1-40 with no special characters
    #@require phone is all digits, length of 10, doesn't start with 0, 1, or 2
    #@require address is an address object 
    def __init__(self, first: str, last: str, phone: int, address: Address, initialAccountType: str) -> 'Client':
        assert isinstance(first, str) and first.isprintable() and 1 <= len(first) <= 25, 'invalid first name'
        assert isinstance(last, str) and last.isprintable() and 1 <= len(last) <= 40, 'invalid last name'
        assert phone.isdecimal() and len(phone) == 10 and not phone[0] in ["0", "1", "2"] and all([int(i) in range(10) for i in phone]), "invalid phone number"
        #attempt to cast phone num to int, throw assertion error if it fails. 
        #this way it accepts strings, floats, and ints so long as it's castable to int  
        # try:
        #     phone = int(phone)
        # except:
        #     assert False, 'invalid phone number'
        # phonestr = str(phone)
        # assert len(phonestr) == 10 and not phonestr[0] in ['0','1','2'] and all([int(i) in range(10) for i in phonestr]), 'invalid phone number'
        assert isinstance(address, Address)
        
        self._first = first
        self._last = last
        self._phone = phone
        self._address = address
        self._accounts = []
        self._clientNumber = Client._nextClientNumber
        self._nextAccountNumber = 1000
        #increment the next client number 
        Client._nextClientNumber += 1
        self.openAccount(initialAccountType)
    
    # getFirstName returns the client's first name 
    # @return: the client's first name
    def getFirstName(self) -> str:
        return self._first
    
    # getLastName returns the client's last name 
    # @return: the client's last name
    def getLastName(self) -> str:
        return self._last
    
    # getClientNumber returns the client's client number 
    # @return: the client's client number
    def getClientNumber(self) -> int:
        return self._clientNumber
    
    #print all of the client details, including the accounts and their transactions 
    def printClient(self) -> None:
        print(f'First Name: {self._first}\nLast Name: {self._last}\nPhone Number: {self._phone}\n Address: {str(self._address)}')
        for account in self._accounts:
            print(account)
    
    #updates the first name of the client
    #@param first: new first name string 
    #@require first is a str of length 1-25 with no special characters
    def _setFirstName(self,first:str) -> None:
        assert 1 <= len(first) <= 25 and first.isprintable() and isinstance(first, str), 'invalid first name'
        self._first = first
    
    #updates the last name of the client
    #@param last: new last name string 
    #@require last is a str of length 1-40 with no special characters
    def _setLastName(self,last:'str') -> None:
        assert 1 <= len(last) <= 40 and last.isprintable() and isinstance(last, str), 'invalid last name'
        self._last = last
    
    #creates a new account and adds it to the client's list of accounts
    #@param type: the type of the new account, as a string 
    #@require type is a string in bankaccount's account types 
    def openAccount(self,type:str) -> None:
        assert isinstance(type,str) and type in BankAccount.ACCOUNT_TYPES
        if type == 'Checking':
            self._accounts.append(CheckingAccount(self._nextAccountNumber,self._first,self._last))
        elif type == 'Savings':
            self._accounts.append(SavingsAccount(self._nextAccountNumber,self._first,self._last))
        self._nextAccountNumber += 1 

    #closes the account and withdrawing all the funds
    def closeAccount(self,number) -> None:
        pass

# if __name__ == "__main__":
#     client = Client('timmy','smith',9123456789,Address('timmydrive','glenallen','VA'))
#     client.printClient()
