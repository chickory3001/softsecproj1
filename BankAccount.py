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
    
    #constructs a bank account object
    #@param first: the first name as a string, default empty string 
    #@param last: the last name as a string, default empty string
    #@require first is a str of length 1-25 with no special characters
    #@require last is a str of length 1-40 with no special characters
    #@ensure account number >= 1000
    def __init__(self, first: str = "", last: str =""):
        assert isinstance(first, str) and first.isalpha() and 1 <= len(first) <= 25, 'invalid first name'
        assert isinstance(last, str) and last.isalpha() and 1 <= len(last) <= 40, 'invalid last name'
    
        self._first = first
        self._last = last
        self._accountNumber = BankAccount._nextAccountNumber
        self._transactions = []
        self._timesOverdrawn = 0
    
        # Increment the next account number. 
        BankAccount._nextAccountNumber += 1
        assert self._accountNumber >= 1000, 'account number must be >= 1000'

    
    ### QUERIES ###
    
    # getFirst returns the account's first name 
    # @return: the account's first name
    def getFirst(self) -> str:
        return self._first
    
    # getLast returns the account's last name 
    # @return: the account's last name
    def getLast(self) -> str:
        return self._last
    
    # getBalance returns the account's balance 
    # @return: the sum of the transactions list
    def getBalance(self) -> float:
        return 0 + float(sum(self._transactions))
    
    # getAccountNumber returns the account's account number 
    # @return: the account's accunt number
    def getAccountNumber(self) -> int:
        return self._accountNumber
    
    # getTransactions returns the account's transactions list 
    # @return: the account's transaction list
    def getTransactions(self) -> list[Transaction]:
        return self._transactions
    
    # getTimesOverdrawn returns the account's amount of times overdrawn 
    # @return: the account's amount of times overdrawn
    def getTimesOverdrawn(self) -> int:
        return self._timesOverdrawn

    #prints all of the account's instance variables 
    def printAccount(self):
        print(str(self))
    
    #prints the list of transactions for the account 
    def printTransactions(self):
        #iterate over the list of transactions
        for x in self._transactions:
            print(str(x))


    ### COMMANDS ###
    
    #updates the first name of the account
    #@param first: new first name string 
    #@require first is a str of length 1-25 with no special characters
    def _setFirstName(self,first:str):
        assert 1 <= len(first) <= 25 and first.isalpha and isinstance(first, str), 'invalid first name'
        self._first = first
    
    #updates the last name of the account
    #@param last: new last name string 
    #@require last is a str of length 1-40 with no special characters
    def _setLastName(self,last:'str'):
        assert 1 <= len(last) <= 25 and last.isalpha and isinstance(last, str), 'invalid last name'
        self._last = last
    
    #adds 1 to the timesOverdrawn counter variable 
    def _incrementOverdraft(self):
        self._timesOverdrawn += 1
    
    #deposits money into the account via creating a deposit transaction
    #@param amount: amount to deposit 
    #@require amount > 0 
    def deposit(self,amount:float):
        assert (isinstance(amount, float) or isinstance(amount, int)) and amount > 0.0, 'invalid deposit amount'
        self._transactions.append(Transaction(len(self._transactions)+1, 'deposit', amount))
    
    #calculates and adds interest into the account via creating an interest transaction
    def addInterest(self):
        # don't do interest on negative balance, since it would be negative interest
        if self.getBalance() > 0:
            interest = self.getBalance() * BankAccount.INTEREST_RATE
            self._transactions.append(Transaction(len(self._transactions)+1, 'interest', interest))
    
    #withdraws money from the account via creating a withdraw transaction
    #@param amount: amount to withdraw 
    #@require amount > 0 
    def withdraw(self, amount: float) -> bool:
        assert amount > 0, 'invalid withdrawal amount'
        if amount > self.getBalance()+250:
            print("Transaction denied")
            return False
        elif self.getBalance() > 0.0:
            withdrawalTransaction = Transaction(len(self._transactions)+1, "withdrawal", -amount)
            self._transactions.append(withdrawalTransaction)
            # Subtract from balance by amount
            if self.getBalance() < 0:
                self._incrementOverdraft()
                penaltyTransaction = Transaction(len(self._transactions)+1, "penalty", -BankAccount.OVERDRAFT_FEE)
                print("Account has been overdrawn")
                self._transactions.append(penaltyTransaction)
            return True 
        else:
            print("Transaction denied")
            return False
    
    #withdraws money from the other account and deposits it into self
    #via withdrawing from other and depositing into self
    #@param amount: amount to transfer to the account 
    #@require amount > 0 
    def transfer(self, other: 'BankAccount', amount: float) -> bool:
        assert amount > 0, 'invalid transfer amount'
        # if the withdrawal from the other account is successful, deposit the amount into self
        if other.withdraw(amount):
            self.deposit(amount)
            return True
        # if it's unsuccessful, don't deposit
        else:
            return False

    
    ### Special Methods ###
    
    # Returns a string containing the account instance variables.
    # @return: The formatted, human readable string of the account 
    def __str__(self) -> str:
        string = (f'First Name: {self._first}\nLast Name: {self._last}\n'
            f'Account Number: {self._accountNumber}\nBalance: {self.getBalance()}')
        #iterate over list of transactions, puts newline before to ensure there's no trailing newline char
        for x in self._transactions:
            string += '\n' + str(x) 
        return string
    
    # Returns a string containing the account instance variables.
    # @return: The formatted, machine readable string of the account 
    def __repr__(self) -> str:
        string = (f'BankAccount(first : {self._first}, last : {self._last}, '
            f'accountNumber : {self._accountNumber}, timesOverdrawn : {self._timesOverdrawn}, transactions : [')
        #iterate over list of transactions, puts newline before to ensure there's no trailing newline char
        for x in self._transactions:
            string += '\n' + repr(x) 
        string += '])'
        #use : instead of = because McManus said so 
        string = string.replace('=',':')
        return string
    
    #checks to see if two accounts have the same account number
    #@param other: the account obj being compared to 
    #@return true if the account numbers are the same, false if not 
    def __eq__(self,other:'BankAccount') -> bool:
        return self._accountNumber == other._accountNumber
    
    #checks if this account's account number is less than the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is less than other, false if otherwise
    def __lt__(self,other:'BankAccount') -> bool:
        return self._accountNumber < other._accountNumber
    
    #checks if this account's account number is greater than the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is greater than other, false if otherwise
    def __gt__(self,other:'BankAccount') -> bool:
        return self._accountNumber > other._accountNumber
    
    #checks if this account's account number is less than or equal to the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is less than or equal to other, false if otherwise
    def __le__(self,other:'BankAccount') -> bool:
        return self._accountNumber <= other._accountNumber
    
    #checks if this account's account number is greater than or equal to the other
    #@param other: the account obj being compared to
    #@return true if this account's account number is greater than or equal to other, false if otherwise
    def __ge__(self,other:'BankAccount') -> bool:
        return self._accountNumber >= other._accountNumber


        
    

if __name__ == "__main__":
    account = BankAccount('joe','shmoe')
    account.deposit(100.0)
    account.deposit(1000.0)
    account.printAccount()
    print()
    # print(repr(account._transactions[0]))
    print(repr(account))
    # account.printTransactions()
    BankAccount('!@#$%^&*','smith')

