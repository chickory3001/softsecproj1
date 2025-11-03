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

# checking account subclass extends BankAccount
class CheckingAccount(BankAccount):
    INTEREST_RATE = 0.015 #overrides BankAccount's interest rate
    ENCRYPTIONKEY = b'MySuperSecretKey2222222222222222' 
    ENCRYPTIONIV = b'MySuperSecretIV0'  
    def __init__(self, number: int) -> 'CheckingAccount':
        super().__init__('Checking',number)


    #deposits money into the account via creating a deposit transacation
    #@para amount: amount to deposit
    #@require amount > 0
    def deposit(self, amount):
        assert amount > 0 and amount != 0, "Enter amount greater than 0 to deposit into account"
        self.getBalance = self.getBalance + amount
    
    #withdraws money from the account via creating a withdraw transaction
    #@param amount: amount to withdraw 
    #@require amount > 0 
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
        else:
            print("Transaction Denied")
            return False
    
    #encrypts and writes transactions to checking.txt
    def writeTransactions(self) -> None:
        string = ''
        for transaction in self._transactions:
            string += str(transaction)
        # encrypt the string
        encrypted_text = encrypt_AES_CBC(string, CheckingAccount.ENCRYPTIONKEY, CheckingAccount.ENCRYPTIONIV)  
        # write raw bytes to text file 
        with open("checking.txt", "wb") as f:
            f.write(encrypted_text)
    
    #reads, decrypts, and prints transactions from checking.txt
    def readTransactions(self) -> None:
            # read raw bytes back
        with open("checking.txt", "rb") as f:
            filedata = f.read()
        # Decrypt the encrypted text
        decrypted_text = decrypt_AES_CBC(filedata, CheckingAccount.ENCRYPTIONKEY, CheckingAccount.ENCRYPTIONIV)  
        print(decrypted_text)

# if __name__ == "__main__":
#     account = CheckingAccount(1000)
#     account.deposit(1000000)
#     account.addInterest()
#     account.withdraw(100)
#     print(str(account))
#     account.printTransactions()
#     account.printAccount()
