# CheckingAccount.py
# 
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 2
# 
# This module defines the CheckingAccount class.

from BankAccount import BankAccount
from transaction import Transaction 
from AES_CBC import *
from base64 import b64encode, b64decode
from os import urandom

# Checking account subclass extends BankAccount
class CheckingAccount(BankAccount):
    
    # Class constants
    INTEREST_RATE = 0.015   # Overrides BankAccount's interest rate
    
    def __init__(self, number: int) -> 'CheckingAccount':
        super().__init__('c',number)
        self._ENCRYPTIONKEY = urandom(32)
        self._ENCRYPTIONIV = urandom(16)

    # Withdraws money from the account via creating a withdraw transaction
    # @param amount: amount to withdraw 
    # @require amount > 0 
    def withdraw(self, amount: float) -> bool:
        assert isinstance(amount,(int,float)) and amount > 0, 'invalid withdrawal amount'
        if amount > self.getBalance():
            print("Transaction Denied")
            return False
        elif self.getBalance() > 0.0:
            # Subtract from balance by amount
            withdrawalTransaction = Transaction(len(self._transactions)+BankAccount.STARTING_TRANSACTION_NUMBER, "withdrawal", -amount)
            self._transactions.append(withdrawalTransaction)
            return True 

