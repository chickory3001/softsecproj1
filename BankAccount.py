# bankaccount.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 1
# 
# This module defines the BankAccount class.
# A class to represent a secure bank account.

from transaction import Transaction

class BankAccount:
    _overdraft = 20.00
    _interest = 0.075 # interest as a decimal 
    _nextAccountNumber = 1000

    def __init__(self, first:str = "", last:str ="", balance:float = 0.0):
        assert 1 <= len(first) <= 25 and first.isalpha and isinstance(first, str), 'invalid first name'
        assert 1 <= len(last) <= 40 and last.isalpha and isinstance(last, str), 'invalid last name'
        assert isinstance(balance,float),'invalid balance'

        self._first = first
        self._last = last
        self._balance = balance
        self._accountNumber = BankAccount._nextAccountNumber
        self._transactions = []
        self._timesOverdrawn = 0

        # increment the next account number 
        BankAccount._nextAccountNumber += 1
    
    # getFirst returns the account's first name 
    # @return: the account's first name
    def getFirst(self) :
        return self._first
    
    # getLast returns the account's last name 
    # @return: the account's last name
    def getLast(self) :
        return self._last
    
    # getBalance returns the account's balance 
    # @return: the account's balance
    def getBalance(self) :
        return self._balance
    
    # getAccountNumber returns the account's account number 
    # @return: the account's accunt number
    def getAccountNumber(self) :
        return self._accountNumber
    
    # getTransactions returns the account's transactions list 
    # @return: the account's transaction list
    def getTransactions(self) :
        return self._transactions
    
    # getTimesOverdrawn returns the account's amount of times overdrawn 
    # @return: the account's amount of times overdrawn
    def getTimesOverdrawn(self) :
        return self._timesOverdrawn
    
    def deposit(self,amount:float):
        assert isinstance(amount,float) and amount >= 0.0, 'invalid deposit amount'
        self._transactions.append(Transaction(len(self._transactions)+1,'deposit',amount))
        self._balance += amount
    
    def interest(self):
        interest = self._balance * BankAccount._interest
        self._transactions.append(Transaction(len(self._transactions)+1,'interest',interest))
        self._balance += interest


print(BankAccount._nextAccountNumber)
account = BankAccount('joe','shmoe')
print(BankAccount._nextAccountNumber)

