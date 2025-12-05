# SavingsAccount.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 2
# 
# This module defines the SavingsAccount class.

from BankAccount import BankAccount
from transaction import Transaction 
from AES_CBC import *
from base64 import b64encode, b64decode
from os import urandom

# Savings account subclass extends BankAccount
class SavingsAccount(BankAccount):
    
    # Class constants
    INTEREST_RATE = 0.04 # Overrides BankAccount's interest rate
    OVERDRAFTFEE = [20,30,50]
    
    def __init__(self, number: int) -> 'SavingsAccount':
        super().__init__('s',number)
        self._ENCRYPTIONKEY = urandom(32)
        self._ENCRYPTIONIV = urandom(16)
    
    # Withdraws money from the account via creating a withdraw transaction
    # @param amount: amount to withdraw 
    # @require amount > 0 
    def withdraw(self, amount: float) -> bool:
        assert isinstance(amount,(int,float)) and amount > 0, 'invalid withdrawal amount'

        # If there isn't enough and times overdrawn are past 3 times, to deny the withdraw
        if amount > self.getBalance()+250 or self._timesOverdrawn >= 3:
            print("Transaction denied")
            if self._timesOverdrawn >= 3:
                print("Too many overdrafts, raise balance to 100$ to withdraw")
            return False

        # If the balanace is correct, check if it has overdraw fees
        elif self.getBalance() > 0.0:
            # Transaction is approved
            withdrawalTransaction = Transaction(len(self._transactions)+1, "withdrawal", -amount)
            self._transactions.append(withdrawalTransaction)
            
            # If the withdrawal overdrafts
            if self.getBalance() < 0:
                print("Overdraft charge has been added to account")
                penaltyTransaction = Transaction(len(self._transactions)+1, "penalty", -SavingsAccount.OVERDRAFTFEE[self._timesOverdrawn])
                self._transactions.append(penaltyTransaction)
                self._incrementOverdraft()
            
            return True 
        else:
            print("Transaction denied")
            return False
    
    # Deposits money into the account via creating a deposit transaction
    # @param amount: amount to deposit 
    # @require amount > 0 
    # deposit is redefined here to implement special logic with the overdraw counter, checkingaccount doesn't 
    # implement it 
    def deposit(self,amount:float):
        assert (isinstance(amount, float) or isinstance(amount, int)) and amount > 0.0, 'invalid deposit amount'
        
        prevBalance = self.getBalance()
        self._transactions.append(Transaction(len(self._transactions)+BankAccount.STARTING_TRANSACTION_NUMBER, 'deposit', amount))
        currentBalance = self.getBalance()
        
        # Removes one of the overdraft violation
        if prevBalance < 100 and currentBalance >= 100 and self._timesOverdrawn > 0:
            self._timesOverdrawn -= 1
        
        # Removes all overdraft violations
        if prevBalance < 10000 and currentBalance >= 10000:
            self._timesOverdrawn = 0
            print("Overdraft fees have been reset")
