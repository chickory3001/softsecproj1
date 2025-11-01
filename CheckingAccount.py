from BankAccount import BankAccount
from transaction import Transaction 

class CheckingAccount(BankAccount):
    INTEREST_RATE = 0.015
    def __init__(self, number: int) -> 'CheckingAccount':
        super().__init__('Checking',number)

    #withdraws money from the account via creating a withdraw transaction
    #@param amount: amount to withdraw 
    #@require amount > 0 
    def withdraw(self, amount: float) -> bool:
        assert amount > 0, 'invalid withdrawal amount'
        if amount > self.getBalance():
            print("Transaction denied")
            return False
        elif self.getBalance() > 0.0:
            # Subtract from balance by amount
            withdrawalTransaction = Transaction(len(self._transactions)+1, "withdrawal", -amount)
            self._transactions.append(withdrawalTransaction)
            return True 
        else:
            print("Transaction denied")
            return False