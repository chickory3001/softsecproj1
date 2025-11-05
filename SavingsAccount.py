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
    OVERDRAFTFEE = [20,30,50]
    def __init__(self, number: int) -> 'SavingsAccount':
        super().__init__('Savings',number)
    
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
            if self._timesOverdrawn == 3:
                print("Too many overdraft fees have occurred, transacation denied")
                return False
            withdrawalTransaction = Transaction(len(self._transactions)+1, "withdrawal", -amount)
            self._transactions.append(withdrawalTransaction)
            # if the withdrawal overdrafts
            if self.getBalance() < 0:
                print("Overdraft charge has been added to account OVERDRAFTFEE[self._timesOverdrawn]")
                penaltyTransaction = Transaction(len(self._transactions)+1, "penalty", -SavingsAccount.OVERDRAFTFEE[self._timesOverdrawn])
                self._transactions.append(penaltyTransaction)
                self._timesOverdrawn = self._timesOverdrawn + 1 
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
            print("Overdraft fees have been reset")


    
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
    
    #reads the transaction data from the file, decrypts it, and returns it 
    def getTransactionData(self) -> str:
            # read raw bytes back
        with open("savings.txt", "rb") as f:
            filedata = f.read()
        # Decrypt the encrypted text
        decrypted_text = decrypt_AES_CBC(filedata, SavingsAccount.ENCRYPTIONKEY, SavingsAccount.ENCRYPTIONIV)  
        return decrypted_text
    
    #prints the transaction data from file 
    def readTransactions(self) -> None:
        print(self.getTransactionData())

    # prints transactions to standard output
    def printTransactions(self) -> None:
    	
    	# Create an empty string
    	string = ""
    	
    	# Add each transaction to the string alongside a newline character
    	for transaction in self._transactions:
    		string += str(transaction) + "\n"
    		
    	# Print the string
    	print(string)

# if __name__ == "__main__":
