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
    OVERDRAFT_FEE1 = 20
    OVERDRAFT_FEE2 = 30
    OVERDRAFT_FEE3 = 50
    def __init__(self, number: int) -> 'SavingsAccount':
        super().__init__('Savings',number)
    
    #deposits money into the account via creating a depsoit transacation
    #@para amount: amount to deposit
    #@require amount > 0
    def deposit(self, amount):
        assert amount > 0, "Enter amount to deposit must be more than 0"
        self.getBalance = self.getBalance + amount
    
    #withdraws money from the account via creating a withdraw transaction
    #@param amount: amount to withdraw 
    #@require amount > 0 
    def withdraw(self, amount: float) -> bool:
        assert isinstance(amount,(int,float)) and amount > 0, 'invalid withdrawal amount'
        if amount > self.getBalance()+250 or self._timesOverdrawn >= 3:
            print("Transaction denied")
            if self._timesOverdrawn >= 3:
                print("Too many overdrafts, raise balance to 100$ to withdraw")
            return False
        elif self.getBalance() > 0.0:
            # Subtract from balance by amount
            withdrawalTransaction = Transaction(len(self._transactions)+1, "withdrawal", -amount)
            self._transactions.append(withdrawalTransaction)
            # if the withdrawal overdrafts
            if self.getBalance() < 0:
                self._incrementOverdraft()
                if self._timesOverdrawn == 1:
                    penaltyTransaction = Transaction(len(self._transactions)+1, "penalty", -SavingsAccount.OVERDRAFT_FEE1)
                elif self._timesOverdrawn == 2:
                    penaltyTransaction = Transaction(len(self._transactions)+1, "penalty", -SavingsAccount.OVERDRAFT_FEE2)
                elif self._timesOverdrawn == 3:
                    penaltyTransaction = Transaction(len(self._transactions)+1, "penalty", -SavingsAccount.OVERDRAFT_FEE3)
                print("Account has been overdrawn")
                self._transactions.append(penaltyTransaction)
            return True 
        else:
            print("Transaction denied")
            return False
    
    #deposits money into the account via creating a deposit transaction
    #@param amount: amount to deposit 
    #@require amount > 0 
    def deposit(self,amount:float) -> None:
        assert (isinstance(amount, float) or isinstance(amount, int)) and amount > 0.0, 'invalid deposit amount'
        prevBalance = self.getBalance()
        self._transactions.append(Transaction(len(self._transactions)+BankAccount.STARTING_TRANSACTION_NUMBER, 'deposit', amount))
        currentBalance = self.getBalance()
        if prevBalance < 100 and currentBalance >= 100 and self._timesOverdrawn > 0:
            self._timesOverdrawn -= 1
        if prevBalance < 10000 and currentBalance >= 10000:
            self._timesOverdrawn = 0

    #adds interests to the savings account
    def interest(self):
        self.getBalance = self.getBalance + (self.getBalance * INTEREST_RATE)
    
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
