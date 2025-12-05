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
    
    # Encrypts and writes transactions to savings.txt
    def _writeTransactions(self):
        string = ''
        for transaction in self._transactions:
            string += str(transaction)
        
        # Encrypt the string
        encrypted_text = encrypt_AES_CBC(string, self._ENCRYPTIONKEY, self._ENCRYPTIONIV)  
        
        # Write raw bytes to text file 
        with open("checking.txt", "wb") as f:
            f.write(encrypted_text)
    
    # Reads the transaction data from the file, decrypts it, and returns it 
    def _getTransactionData(self) -> str:
            
            # Read raw bytes back
        with open("checking.txt", "rb") as f:
            filedata = f.read()
        
        # Decrypt the encrypted text
        decrypted_text = decrypt_AES_CBC(filedata, self._ENCRYPTIONKEY, self._ENCRYPTIONIV)  
        return decrypted_text
    
    # Prints the transaction data from file 
    def _readTransactions(self):
        print(self._getTransactionData())
