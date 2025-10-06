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
    OVERDRAFT_FEE = 20.00
    INTEREST_RATE = 0.075
    _nextAccountNumber = 1000

    def __init__(self, first: str = "", last: str =""):
        assert 1 <= len(first) <= 25 and first.isalpha and isinstance(first, str), 'invalid first name'
        assert 1 <= len(last) <= 40 and last.isalpha and isinstance(last, str), 'invalid last name'
        assert isinstance(balance,float),'invalid balance'

        self._first = first
        self._last = last
        self._accountNumber = BankAccount._nextAccountNumber
        self._transactions = []
        self._timesOverdrawn = 0

        # Increment the next account number. 
        BankAccount._nextAccountNumber += 1

    ### QUERIES ###
    
    # getFirst returns the account's first name 
    # @return: the account's first name
    def getFirst(self):
        return self._first
    
    # getLast returns the account's last name 
    # @return: the account's last name
    def getLast(self):
        return self._last
    
    # getBalance returns the account's balance 
    # @return: the account's balance
    def getBalance(self):
        return sum(self._transactions)
    
    # getAccountNumber returns the account's account number 
    # @return: the account's accunt number
    def getAccountNumber(self):
        return self._accountNumber
    
    # getTransactions returns the account's transactions list 
    # @return: the account's transaction list
    def getTransactions(self):
        return self._transactions
    
    # getTimesOverdrawn returns the account's amount of times overdrawn 
    # @return: the account's amount of times overdrawn
    def getTimesOverdrawn(self):
        return self._timesOverdrawn


    ### COMMANDS ###
    
    def deposit(self,amount:float):
        assert isinstance(amount,float) and amount >= 0.0, 'invalid deposit amount'
        self._transactions.append(Transaction(len(self._transactions)+1, 'deposit', amount))
        self._balance += amount
    
    def addInterest(self):
        interest = self._balance * BankAccount._interest
        self._transactions.append(Transaction(len(self._transactions)+1, 'interest', interest))
        self._balance += interest

    def withdraw(self, amount: float):
        if amount > self.getBalance()+250:
            print("Transaction denied")
        elif amount >= 0:
            withdrawalTransaction = Transaction(len(self._transactions)+1, "withdrawal", amount)
            self._transactions.append(withdrawalTransaction)
            # Subtract from balance by amount
            if self.getBalance() < 0:
                self._incrementOverdraft()
                penaltyTransaction = Transaction(len(self._transactions)+1, "penalty", -OVERDRAFT_FEE)
                print("Account has been overdrawn")
                self._transactions.append(penaltyTransaction)
        else:
            print("Transaction denied")
    
    def _incrementOverdraft(self):
        self._timesOverdrawn += 1

    def transfer(self, other, amount: float):
        pass


if __name__ == "__main__":
    print(BankAccount._nextAccountNumber)
    account = BankAccount('joe','shmoe')
    print(BankAccount._nextAccountNumber)

