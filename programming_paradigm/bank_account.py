
class BankAccount: 
    def __init__(self,account_balance = 0): 
        """initializing a balance parameter with default value of zero"""
        self.account_balance = account_balance 

    def deposit(self,amount): 
        """Implementing a deposit method that add money to the account_balance"""
        self.account_balance += amount 

    def withdraw(self,amount): 
        """Implementing a withdraw method that withdraw money from the account if sufficient funds are available."""
        if amount <= self.account_balance : 
            self.account_balance -= amount 
            return True 
        else : 
            return False     #The return statement checks if the account balance is sufficient for withdrawal  
                             #if sufficent , return True , else False . 

    def display_balance(self): 
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")   


