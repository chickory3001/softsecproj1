# bankaccount.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 1
# 
# This module defines the BankAccount class.
# A class to represent a secure bank account.

from transaction import Transaction
from abc import ABC, abstractmethod

class BankAccount:
    OVERDRAFT_FEE = 20.00
    INTEREST_RATE = 0.075
    ACCOUNT_TYPES = ['Checking','Savings']
    _nextAccountNumber = 1000
    
    #constructs a bank account object
    #@param type the type of account
    #@require type is in the allowed ACCOUNT_TYPES list 
    #@ensure account number >= 1000
    def __init__(self,type) -> 'BankAccount':
        assert type in BankAccount.ACCOUNT_TYPES, 'invalid account type'
        self._accountNumber = BankAccount._nextAccountNumber
        self._transactions = []
        self._timesOverdrawn = 0
    
        # Increment the next account number. 
        BankAccount._nextAccountNumber += 1
        assert self._accountNumber >= 1000, 'account number must be >= 1000'
    
    
    ### QUERIES ###
    
    # getBalance returns the account's balance 
    # @return: the sum of the transactions list
    def getBalance(self) -> float:
        return 0 + float(sum(self._transactions))
    
    # getAccountNumber returns the account's account number 
    # @return: the account's accunt number
    def getAccountNumber(self) -> int:
        return self._accountNumber
    
    # getTransactions returns the account's transactions list 
    # @return: the account's transaction list
    def getTransactions(self) -> list[Transaction]:
        return self._transactions
    
    # getTimesOverdrawn returns the account's amount of times overdrawn 
    # @return: the account's amount of times overdrawn
    def getTimesOverdrawn(self) -> int:
        return self._timesOverdrawn

    #prints all of the account's instance variables 
    def printAccount(self) -> None:
        print(str(self))
    
    #prints the list of transactions for the account 
    def printTransactions(self) -> None:
        #iterate over the list of transactions
        for x in self._transactions:
            print(str(x))
    
    ### COMMANDS ###
    
    #adds 1 to the timesOverdrawn counter variable 
    def _incrementOverdraft(self) -> None:
        self._timesOverdrawn += 1
    
    #deposits money into the account via creating a deposit transaction
    #@param amount: amount to deposit 
    #@require amount > 0 
    def deposit(self,amount:float) -> None:
        assert (isinstance(amount, float) or isinstance(amount, int)) and amount > 0.0, 'invalid deposit amount'
        self._transactions.append(Transaction(len(self._transactions)+1, 'deposit', amount))
    
    #calculates and adds interest into the account via creating an interest transaction
    def addInterest(self) -> None:
        # don't do interest on negative balance, since it would be negative interest
        if self.getBalance() > 0:
            interest = self.getBalance() * BankAccount.INTEREST_RATE
            self._transactions.append(Transaction(len(self._transactions)+1, 'interest', interest))
    
    #withdraws money from the account via creating a withdraw transaction
    #to be implemented by the subclasses checking account and savings account
    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        pass
    
    #withdraws money from the other account and deposits it into self
    #via withdrawing from other and depositing into self
    #to be implemented by the subclasses checking account and savings account
    @abstractmethod
    def transfer(self, other: 'BankAccount', amount: float) -> bool:
        pass
    
    ### Special Methods ###
    
    # Returns a string containing the account instance variables.
    # @return: The formatted, human readable string of the account 
    def __str__(self) -> str:
        string = (f'Account Number: {self._accountNumber}\nBalance: {self.getBalance()}')
        #iterate over list of transactions, puts newline before to ensure there's no trailing newline char
        for x in self._transactions:
            string += '\n' + str(x) 
        return string
    
    # Returns a string containing the account instance variables.
    # @return: The formatted, machine readable string of the account 
    def __repr__(self) -> str:
        string = (f'BankAccount('
            f'accountNumber : {self._accountNumber}, timesOverdrawn : {self._timesOverdrawn}, transactions : [')
        #iterate over list of transactions, puts newline before to ensure there's no trailing newline char
        for x in self._transactions:
            string += '\n' + repr(x) 
        string += '])'
        #use : instead of = because McManus said so 
        string = string.replace('=',':')
        return string
    
    #checks to see if two accounts have the same account number
    #@param other: the account obj being compared to 
    #@return true if the account numbers are the same, false if not 
    def __eq__(self,other:'BankAccount') -> bool:
        return self._accountNumber == other._accountNumber
    
    #checks if this account's account number is less than the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is less than other, false if otherwise
    def __lt__(self,other:'BankAccount') -> bool:
        return self._accountNumber < other._accountNumber
    
    #checks if this account's account number is greater than the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is greater than other, false if otherwise
    def __gt__(self,other:'BankAccount') -> bool:
        return self._accountNumber > other._accountNumber
    
    #checks if this account's account number is less than or equal to the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is less than or equal to other, false if otherwise
    def __le__(self,other:'BankAccount') -> bool:
        return self._accountNumber <= other._accountNumber
    
    #checks if this account's account number is greater than or equal to the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is greater than or equal to other, false if otherwise
    def __ge__(self,other:'BankAccount') -> bool:
        return self._accountNumber >= other._accountNumber

if __name__ == "__main__":
    pass
