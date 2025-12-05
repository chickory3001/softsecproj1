# bankaccount.py
#
# Created by: J. Bodde, C. Burrell, H. Hickory, R. Pelzel, C. Triplett
# 
# CSEC323 - Project 2
# 
# This module defines the BankAccount class.

from transaction import Transaction
from abc import ABC, abstractmethod
from AES_CBC import * 

# A class to represent a secure bank account 
class BankAccount(ABC):
    INTEREST_RATE = 0.075
    ACCOUNT_TYPES = ['c','s']    # Checking and Savings
    STARTING_TRANSACTION_NUMBER = 100
    NEXTUNIQUEIDENTIFIER = 1
    
    # Constructs a bank account object
    # @param type the type of account
    # @require type is in the allowed ACCOUNT_TYPES list 
    # @require account number >= 1000 and is an int 
    def __init__(self, type: str, number: int) -> 'BankAccount':
        assert type in BankAccount.ACCOUNT_TYPES, 'invalid account type'
        assert isinstance(number, int) and number >= 1000, 'account number must be >= 1000 and type int'
        self._accountNumber = number
        self._transactions = []
        self._timesOverdrawn = 0
        self._type = type
        self._id = BankAccount.NEXTUNIQUEIDENTIFIER
        BankAccount.NEXTUNIQUEIDENTIFIER += 1
    
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
    
    # getId returns the account's id number 
    # @return: the account's account type as a string
    def getId(self) -> 'str':
        return self._id
    
    # getTransactions returns the account's transactions list 
    # @return: the account's transaction list
    def getTransactions(self) -> list[Transaction]:
        return self._transactions
    
    # getTimesOverdrawn returns the account's amount of times overdrawn 
    # @return: the account's amount of times overdrawn
    def getTimesOverdrawn(self) -> int:
        return self._timesOverdrawn
    
    # Prints all of the account's instance variables 
    def printAccount(self):
        print(str(self))
    
    # Prints the list of transactions for the account 
    def printTransactions(self):
        
        # Iterate over the list of transactions
        for x in self._transactions:
            print(str(x))
    
    
    ### COMMANDS ###
    
    # Adds 1 to the timesOverdrawn counter variable 
    def _incrementOverdraft(self):
        self._timesOverdrawn += 1
    
    # Deposits money into the account via creating a deposit transaction
    # @param amount: amount to deposit 
    # @require amount > 0 
    def deposit(self,amount:float):
        assert (isinstance(amount, float) or isinstance(amount, int)) and amount > 0.0, 'invalid deposit amount'
        self._transactions.append(Transaction(len(self._transactions)+BankAccount.STARTING_TRANSACTION_NUMBER, 'deposit', amount))
    
    # Calculates and adds interest into the account via creating an interest transaction
    # @require balance > 0 
    def addInterest(self):
        
        # Don't do interest on negative balance, since it would be negative interest
        assert self.getBalance() > 0, 'can\'t add interest with balance <= 0'
        interest = self.getBalance() * self.__class__.INTEREST_RATE
        self._transactions.append(Transaction(len(self._transactions)+BankAccount.STARTING_TRANSACTION_NUMBER, 'interest', interest))
    
    # Withdraws money from the account via creating a withdraw transaction
    # To be implemented by the subclasses checking account and savings account
    @abstractmethod
    def withdraw(self, amount: float) -> bool: # pragma: no cover 
        # coverage will inevitably miss this since this it is abstract, 
        # so the comment above tells coverage to ignore it
        # just so i can see 100% 
        pass
    
    # Withdraws money from the other account and deposits it into self
    # via withdrawing from other and depositing into self
    # @param amount: amount to transfer to the account 
    # @require amount > 0 
    def transfer(self, other: 'BankAccount', amount: float) -> bool:
        assert isinstance(amount,(int,float)) and amount > 0, 'invalid transfer amount'
        assert other is not self, 'cannot transfer to the same account'
        
        # If the withdrawal from the other account is successful, deposit the amount into self
        if other.withdraw(amount):
            self.deposit(amount)
            return True
        
        # If it's unsuccessful, don't deposit
        return False
    
    # Encrypts and writes transactions to respective txt file 
    def _writeTransactions(self):
        string = ''
        for transaction in self._transactions:
            string += str(transaction)
        
        # Encrypt the string
        encrypted_text = encrypt_AES_CBC(string, self._ENCRYPTIONKEY, self._ENCRYPTIONIV)  
        
        # Write raw bytes to text file 
        if self._type == 'c':
            with open("checking.txt", "wb") as f:
                f.write(encrypted_text)
        elif self._type == 's':
            with open("savings.txt", "wb") as f:
                f.write(encrypted_text)
    
    # Reads the transaction data from the file, decrypts it, and returns it 
    def _getTransactionData(self) -> str:
        
            # Read raw bytes back
        if self._type == 'c':
            with open("checking.txt", "rb") as f:
                filedata = f.read()
        elif self._type == 's':
            with open("savings.txt", "rb") as f:
                filedata = f.read()
        
        # Decrypt the encrypted text
        decrypted_text = decrypt_AES_CBC(filedata, self._ENCRYPTIONKEY, self._ENCRYPTIONIV)  
        return decrypted_text
    
    # Prints the transaction data from file 
    def _readTransactions(self):
        print(self._getTransactionData())

    ### SPECIAL METHODS ###
    
    # Returns a string containing the account instance variables.
    # @return: The formatted, human readable string of the account 
    def __str__(self) -> str:
        string = (f'Account Type: {self._type}\nAccount Number: {self._accountNumber}\nBalance: {self.getBalance()}\n Times Overdrawn: {self.getTimesOverdrawn()}\n Id: {self.getId()}')
        
        # Iterate over list of transactions, puts newline before to ensure there's no trailing newline char
        for x in self._transactions:
            string += '\n' + str(x) 
        
        return string
    
    # Returns a string containing the account instance variables.
    # @return: The formatted, machine readable string of the account 
    def __repr__(self) -> str:
        string = (f'BankAccount('
            f'accountNumber : {self._accountNumber}, timesOverdrawn : {self._timesOverdrawn}, transactions : [')
        
        # Iterate over list of transactions, puts newline before to ensure there's no trailing newline char
        for x in self._transactions:
            string += '\n' + repr(x) 
        string += '])'
        
        # Use : instead of = because McManus said so 
        string = string.replace('=',':')
        return string
    
    # Checks to see if two accounts have the same account id
    # @param other: the account obj being compared to 
    # @return true if the account ids are the same, false if not 
    def __eq__(self,other:'BankAccount') -> bool:
        return self._id == other._id
    
    # Checks if this account's account id is less than the other
    # @param other: the account obj being compared to
    # @return true if this account's account id is less than other, false if otherwise
    def __lt__(self,other:'BankAccount') -> bool:
        return self._id < other._id
    
    # Checks if this account's account id is greater than the other
    # @param other: the account obj being compared to
    # @return true if this account's account id is greater than other, false if otherwise
    def __gt__(self,other:'BankAccount') -> bool:
        return self._id > other._id
    
    # Checks if this account's account id is less than or equal to the other
    # @param other: the account obj being compared to
    # @return true if this account's account id is less than or equal to other, false if otherwise
    def __le__(self,other:'BankAccount') -> bool:
        return self._id <= other._id
    
    # Checks if this account's account id is greater than or equal to the other
    # @param other: the account obj being compared to
    # @return true if this account's account id is greater than or equal to other, false if otherwise
    def __ge__(self,other:'BankAccount') -> bool:
        return self._id >= other._id
