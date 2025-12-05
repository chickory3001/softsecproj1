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
from FirstName import FirstName
from LastName import LastName
from Password import Password
from HashedPWD import HashedPWD

# Class to represent a client of a bank 
class Client:
    
    # Client numbers start at 100 
    _nextClientNumber = 100
    
    # Creates a client object 
    # @param first: the first name as a string
    # @param last: the last name as a string 
    # @param phone: the phone number of the client
    # @param address: the address of the client 
    # @require first is a str of length 1-25 with no special characters
    # @require last is a str of length 1-40 with no special characters
    # @require phone is all digits, length of 10, doesn't start with 0, 1, or 2
    # @require address is an address object 
    def __init__(self, first: FirstName, last: LastName, phone: str, address: Address, initialAccountType: str, password: Password) -> 'Client':
        assert isinstance(first, FirstName), 'invalid first name'
        assert isinstance(last, LastName), 'invalid last name'
        assert isinstance(phone, str) and phone.isdecimal() and len(phone) == 10 and not phone[0] in ["0", "1", "2"], "invalid phone number"
        assert isinstance(address, Address), "invalid address"
        assert isinstance(initialAccountType, str) and initialAccountType.lower() in ["c", "s"], "invalid account type"
        assert isinstance(password, Password), 'password must be type Password'
        
        self._first = first
        self._last = last
        self._phone = phone
        self._address = address
        self._accounts = []
        self._clientNumber = Client._nextClientNumber
        self._nextAccountNumber = 1000
        self._hashedpwd = HashedPWD(password)
        
        # Increment the next client number 
        Client._nextClientNumber += 1
        self.openAccount(initialAccountType)
    
    
    ### QUERIES ###
    
    # getFirstName returns the client's first name 
    # @return: the client's first name
    def getFirstName(self) -> str:
        return self._first.getName()
    
    # getLastName returns the client's last name 
    # @return: the client's last name
    def getLastName(self) -> str:
        return self._last.getName()
    
    # getClientNumber returns the client's client number 
    # @return: the client's client number
    def getClientNumber(self) -> int:
        return self._clientNumber
    
    # getPhoneNum returns the client's phone number
    # @return: the client's phone number
    def getPhoneNum(self) -> str:
        return self._phone
    
    # getAddress returns the client's address
    # @return: the client's address as an Address object
    def getAddress(self) -> Address:
        return self._address

    # getHash returns the client's hash
    # @return: the client's hash as a HashedPWD object
    def getAddress(self) -> HashedPWD:
        return self._hash
    
    # Print all of the client details, including the accounts and their transactions 
    def printClient(self):
        print(f'First Name: {self._first}\nLast Name: {self._last}\nPhone Number: {self._phone}\nAddress: {str(self._address)}\nClient Number: {self._clientNumber}\n')
        for account in self._accounts:
            print(account)
    
    
    ### COMMANDS ###
    
    # Updates the first name of the client
    # @param first: new first name string 
    # @require first is a str of length 1-25 with no special characters
    def _setFirstName(self,first:str):
        assert 1 <= len(first) <= 25 and first.isprintable() and isinstance(first, str), 'invalid first name'
        self._first = first
    
    # Updates the last name of the client
    # @param last: new last name string 
    # @require last is a str of length 1-40 with no special characters
    def _setLastName(self,last:'str'):
        assert 1 <= len(last) <= 40 and last.isprintable() and isinstance(last, str), 'invalid last name'
        self._last = last
    
    # Creates a new account and adds it to the client's list of accounts
    # @param type: the type of the new account, as a string 
    # @require type is a string in bankaccount's account types 
    def openAccount(self, type: str):
        assert isinstance(type, str) and type.lower() in ["c", "s"], "invalid account type"
        
        if type.lower() == 'c':
            self._accounts.append(CheckingAccount(self._nextAccountNumber))
        elif type.lower() == 's':
            self._accounts.append(SavingsAccount(self._nextAccountNumber))
            
        self._nextAccountNumber += 1 

    # Closes the account and withdrawing all the funds
    # @param number: the account number, can be obtained using getAccountNumber() method
    # @require number is an int >= 1000 
    def closeAccount(self, number: int) -> bool:
        assert isinstance(number, int), "invalid input for account number"
        assert number >= 1000, "invalid input for account number"
        
        # Loop through the list of accounts until an account number matches
        for i in range(len(self._accounts)):
            if self._accounts[i].getAccountNumber() == number:

                # If the account's balance is negative do not close and return False
                if self._accounts[i].getBalance() < 0:
                    return False

                # Only withdraw if there is a balance in the account
                if self._accounts[i].getBalance() > 0:
                    
                    # Withdraw the current balance of the account
                    self._accounts[i].withdraw(self._accounts[i].getBalance())
                    
                # Remove this account from the client's list of accounts
                self._accounts.pop(i)
                    
                # Return True once completed
                return True
        
        # Return False if the account doesn't exist
        return False
    
    #Changes the password the user wants to enter
    #@Require Password is already associated with an account
    #@Ensure Password is being changed
    def changePassword(self):
        oldPass = input("Enter your previous password")  #Check previous password
        if oldPass != self._password:
            print("Incorrect Previous Password:")
            return False

        #Creation of new password and confirm password
        newPass = input("Enter your new password")
        confirmPass = input("Enter your new password to confirm")
        
        #If the passwords don't match try again
        while newPass != confirmPass:
            print("Passwords do not match, try again:")
            newPass = input("Enter your new password")
            confirmPass = input("Enter your new password to confirm")
        
        #Checks new password to see if it is valid, if not prompt the user to try again
        while not Password.passwordChecker(newPass):
            print("Password invalid try again:")
            newPass = input("Enter your new password")
            confirmPass = input("Enter your new password to confirm")

            while newPass != confirmPass:
                print("Passwords do not match try again:")
                newPass = input("Enter your new password")
                confirmPass = input("Enter your new password to confirm")


        self._password = newPass
        print("Password changed successfully")
        return True

# if __name__ == "__main__":
#     client = Client('timmy', 'smith', '9123456789', Address('323 timmy drive', 'glen allen', 'VA'),'c')
#     client._accounts[0].deposit(100)
#     client.printClient()
