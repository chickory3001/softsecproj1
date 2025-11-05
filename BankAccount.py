# bankaccount.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 2
# 
# This module defines the BankAccount class.
# A class to represent a secure bank account.

from transaction import Transaction
from abc import ABC, abstractmethod

# a class to represent a secure bank account 
class BankAccount(ABC):
    INTEREST_RATE = 0.075
    ACCOUNT_TYPES = ['c','s']    # Checking and Savings
    STARTING_TRANSACTION_NUMBER = 100
    
    # Constructs a bank account object
    #@param type the type of account
    #@require type is in the allowed ACCOUNT_TYPES list 
    #@require account number >= 1000 and is an int 
    def __init__(self, type: str, number: int) -> 'BankAccount':
        assert type in BankAccount.ACCOUNT_TYPES, 'invalid account type'
        assert isinstance(number, int) and number >= 1000, 'account number must be >= 1000 and type int'
        self._accountNumber = number
        self._transactions = []
        self._timesOverdrawn = 0
        self._type = type
    
    ### QUERIES ###
    
    # getBalance returns the account's balance 
    # @return: the sum of the transactions list
    def getBalance(self) -> float:
        return 0.0 + float(sum(self._transactions))
    
    # getAccountNumber returns the account's account number 
    # @return: the account's accunt number
    def getAccountNumber(self) -> int:
        return self._accountNumber
    
    # getType returns the account's account type 
    # @return: the account's account type as a string
    def getType(self) -> 'str':
        return self._type
    
    # getTransactions returns the account's transactions list 
    # @return: the account's transaction list
    def getTransactions(self) -> list[Transaction]:
        return self._transactions
    
    # getTimesOverdrawn returns the account's amount of times overdrawn 
    # @return: the account's amount of times overdrawn
    def getTimesOverdrawn(self) -> int:
        return self._timesOverdrawn
    
    # Prints all of the account's instance variables 
    def printAccount(self) -> None:
        print(str(self))
    
    # Prints the list of transactions for the account 
    def printTransactions(self) -> None:
        #iterate over the list of transactions
        for x in self._transactions:
            print(str(x))
    
    ### COMMANDS ###
    
    # Adds 1 to the timesOverdrawn counter variable 
    def _incrementOverdraft(self) -> None:
        self._timesOverdrawn += 1
    
    # Deposits money into the account via creating a deposit transaction
    #@param amount: amount to deposit 
    #@require amount > 0 
    def deposit(self,amount:float) -> None:
        assert (isinstance(amount, float) or isinstance(amount, int)) and amount > 0.0, 'invalid deposit amount'
        self._transactions.append(Transaction(len(self._transactions)+BankAccount.STARTING_TRANSACTION_NUMBER, 'deposit', amount))
    
    # Calculates and adds interest into the account via creating an interest transaction
    #@require balance > 0 
    def addInterest(self) -> None:
        # don't do interest on negative balance, since it would be negative interest
        assert self.getBalance() > 0, 'can\'t add interest with balance <= 0'
        interest = self.getBalance() * self.__class__.INTEREST_RATE
        self._transactions.append(Transaction(len(self._transactions)+BankAccount.STARTING_TRANSACTION_NUMBER, 'interest', interest))
    
    # Withdraws money from the account via creating a withdraw transaction
    # To be implemented by the subclasses checking account and savings account
    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        pass
    
    # Withdraws money from the other account and deposits it into self
    # via withdrawing from other and depositing into self
    #@param amount: amount to transfer to the account 
    #@require amount > 0 
    def transfer(self, other: 'BankAccount', amount: float) -> bool:
        assert isinstance(amount,(int,float)) and amount > 0, 'invalid transfer amount'
        assert other is not self, 'cannot transfer to the same account'
        # if the withdrawal from the other account is successful, deposit the amount into self
        if other.withdraw(amount):
            self.deposit(amount)
            return True
        # if it's unsuccessful, don't deposit
        return False
    
    ### Special Methods ###
    
    # Returns a string containing the account instance variables.
    # @return: The formatted, human readable string of the account 
    def __str__(self) -> str:
        string = (f'Account Type: {self._type}\nAccount Number: {self._accountNumber}\nBalance: {self.getBalance()}')
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
    
    # Checks to see if two accounts have the same account number
    #@param other: the account obj being compared to 
    #@return true if the account numbers are the same, false if not 
    def __eq__(self,other:'BankAccount') -> bool:
        return self._accountNumber == other._accountNumber
    
    # Checks if this account's account number is less than the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is less than other, false if otherwise
    def __lt__(self,other:'BankAccount') -> bool:
        return self._accountNumber < other._accountNumber
    
    # Checks if this account's account number is greater than the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is greater than other, false if otherwise
    def __gt__(self,other:'BankAccount') -> bool:
        return self._accountNumber > other._accountNumber
    
    # Checks if this account's account number is less than or equal to the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is less than or equal to other, false if otherwise
    def __le__(self,other:'BankAccount') -> bool:
        return self._accountNumber <= other._accountNumber
    
    # Checks if this account's account number is greater than or equal to the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is greater than or equal to other, false if otherwise
    def __ge__(self,other:'BankAccount') -> bool:
        return self._accountNumber >= other._accountNumber

if __name__ == "__main__":
    pass
