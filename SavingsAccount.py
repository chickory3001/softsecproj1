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

# savings account subclass extends BankAccount
class SavingsAccount(BankAccount):
    INTEREST_RATE = 0.04 #overrides BankAccount's interest rate
    ENCRYPTIONKEY = b'MySuperSecretKey2222222222222222' 
    ENCRYPTIONIV = b'MySuperSecretIV0'  
    def __init__(self, number: int) -> 'SavingsAccount':
        super().__init__('Savings',number)
    
    #withdraws money from the account via creating a withdraw transaction
    #@param amount: amount to withdraw 
    #@require amount > 0 
    def withdraw(self, amount: float) -> bool:
        assert isinstance(amount,(int,float)) and amount > 0, 'invalid withdrawal amount'
        pass 
        # get the old withdraw code and modify  
    
    #encrypts and writes transactions to savings.txt
    def writeTransactions(self) -> None:
        string = ''
        for transaction in self._transactions:
            string += str(transaction)
        # encrypt the string
        encrypted_text = encrypt_AES_CBC(string, SavingsAccount.ENCRYPTIONKEY, SavingsAccount.ENCRYPTIONIV)  
        # write raw bytes to text file 
        with open("savings.txt", "wb") as f:
            f.write(encrypted_text)
    
    #reads, decrypts, and prints transactions from savings.txt
    def readTransactions(self) -> None:
            # read raw bytes back
        with open("savings.txt", "rb") as f:
            filedata = f.read()
        # Decrypt the encrypted text
        decrypted_text = decrypt_AES_CBC(filedata, SavingsAccount.ENCRYPTIONKEY, SavingsAccount.ENCRYPTIONIV)  
        print(decrypted_text)

# if __name__ == "__main__":