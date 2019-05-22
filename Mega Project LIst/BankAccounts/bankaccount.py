"""
Code below is a bank account manager for just for 1 person
"""
import random

class Account:
    def __init__(self, balance):
        self.balance = balance
    def __str__(self):
        return f"Account Balance: {self.balance}\n"
    def deposit(self, amount):
        print("Depositing $%.2f" % amount)
        self.balance += amount
    def withdraw(self, amount):
        print("Withdrawing $%.2f" % amount)        
        self.balance -= amount

class Checking(Account):
    def __init__(self, no, balance=0):
        Account.__init__(self, balance)
        self.no = no
    def __str__(self):
        return f"Checking Account #{self.no}: Balance = $%.2f" % self.balance

class Savings(Account):
    def __init__(self, no, balance=0):
        Account.__init__(self, balance)
        self.no = no 
    def __str__(self):
        return f"Savings Account #{self.no}: Balance = $%.2f" % self.balance

class Business(Account):
    def __init__(self, no, balance=0):
        Account.__init__(self, balance)
        self.no = no
    def __str__(self):
        return f"Business Account #{self.no}: Balance = $%.2f" % self.balance

class Customer:
    def __init__(self, name):
        self.name = name
        self.account = []   #would be a list of classes
    
def help_page(name):
    """
    The 'main page' of this 'app'. Asks and returns action to take
    """
    print("Hi {}, how can I help you?".format(name))
    option = int(input("1. Create an account\n2. Look at balance \n3. Withdraw/Deposit \n4. Exit\n"))
    return option

def create():
    """
    Asks for name and returns a account subclass
    """
    print("What account would you like to create?")
    option = int(input("1. Checking Account\n2. Savings Account\n3. Business Account\n4.Exit\n"))
    if option == 1:
        x = random.randint(1000,10000)
        customer = Checking(x)
        print("You have successfully created a checking account! Your account ID is #%d" % x)
        return customer
    elif option == 2:
        x = random.randint(1000,10000)
        customer = Savings(x)
        print("You have successfully created a savings account! Your account ID is #%d" % x)
        return customer
    elif option == 3:
        x = random.randint(1000,10000)
        customer = Business(x)
        print("You have successfully created a business account! Your account ID is #%d" % x)
        return customer
    else:
        print("You have chosen not to create an account")


if __name__=='__main__':
    name = input("Hi, what is your name?")
    customer = Customer(name)
    creation = True
    while creation:
        option = help_page(name)
        if option == 1:                 #create account
            #acc = create()        
            customer.account.append(create())
            print(customer.account)
        elif option == 2:               #look at balance
            if len(customer.account) > 0:
                print("These are your balances")
                for i in customer.account:
                    print(i)
                    print("Balance: $%.2f" % i.balance)
        elif option == 3:       #deposit/withdraw
            try:               
                id = int(input("Which account? (Key in ID) "))
            except:
                print("Enter numerical ID")
            else: 
                for i in customer.account:
                    if i.no == id:
                        while True:
                            choice = input("Deposit or withdraw?\n")
                            amt = int(input("Enter amount"))
                            if choice.lower() == 'deposit':
                                i.deposit(amt)
                            elif choice.lower() == 'withdraw':
                                i.withdraw(amt)
                            break

        elif option == 4:               #exit
            creation = False
    
    print("Thank you! :)")
