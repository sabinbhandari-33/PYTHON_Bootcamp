class bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited", amount)

    def withdraw(self , amount):
        if amount<= self.balance:
            self.balance -= amount
            print("Withdrawn" , amount)
        else:
            print("Insufficient balance.")
    
    def show_balance(self):
        print("Current Balance=",self.balance)


account = bank_account("Sabin", 5000)
account.show_balance()
account.deposit(2000)
account.withdraw(1563)
account.show_balance()
        
