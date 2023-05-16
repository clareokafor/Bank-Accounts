import datetime
import random
class BasicAccount:
    def __init__(self, acName, openingBalance): #Defining the initializers
        if not hasattr(BasicAccount, "acNum"): #If not, the basic account will only have acNum as an attribute in its initialisation.
            BasicAccount.acNum = 0
        BasicAccount.acNum += 1 #This is a designated value for the account number
        self.issueNewCard() 
        self.openingBalance = openingBalance #opening balance is the initial balance of basic account
        self.balance = openingBalance #Hence, self.balance will call the opening balance in this exercise
        self.name = acName #acName is name of the basic account 
        self.acNum = BasicAccount.acNum #the calling of self.acNum will call the account number without having to keep repeating basic account or premium account all the time.
     
     #Defining the methods
    def __str__(self): #Defining the attributes of the basic account as strings
        return f'acName: {self.getName()},cardNum: {self.cardNum}, cardExp: {self.cardExp[0]}/{self.cardExp[1]}, acNum: {self.getAcNum()} Balance: £{self.getAvailableBalance()}'
    
    def deposit(self, amount): #What happens when the bank account is credited what a certain amount of pounds currency.
        if amount < 0: print( f'Amount: £{amount} is invalid') #if the amount in the account is less than zero #This applies to both basic and premium accounts
        self.balance += amount if amount >= 0 else 0.0 #credits the bank account with £
    
    def withdraw(self, amount): #What happens when some pounds is debited from the bank account whether there exist an overdraft or mot
        if (self.getAvailableBalance() >= amount): #available balance in the account is greater than the amount to be withdrawn.
            self.balance = self.balance - amount #withdraws some £ from the account 
            print(self.name, "has withdrawn £" + str(amount) + ". New balance is £" +  str(self.getAvailableBalance()))#shows that the account has been debited with a certain amount  of pounds.
        else:
            print("Can not withdraw £", (amount)) #if there is no money to be withdraw from the account 
            return None
    
    def getAvailableBalance(self): #Getting the available account balance
        return self.balance
    
    def getBalance(self): #Getting the account balance
        return self.balance
    
    def printBalance(self): #Commands to print balance
        print(f'Balance: £{self.getAvailableBalance()}')
        return None
    
    def getName(self): #getting the bank names of Basic and Premium account
        return self.name
    
    def getAcNum(self): #getting the bank numbers of Basic and Premium account
        return str(self.acNum)
    
    def issueNewCard(self): #How to randomly issue a new card to a customer
        exp = datetime.date.today() + datetime.timedelta(days=365*3) #365 days times 3 years is 1095 termed for the duration of expiration.
        self.cardExp = (exp.month,int(str(exp.year)[2:])) #format for month and year of expiration
        self.cardNum = ''.join(random.choices('0123456789',k=16))
    
    def closeAccount(self): #closing the basic account
        if self.getBalance() >= 0: #if the balance in the acocunt is not zero
            self.withdraw(self.getBalance()) #withdraw the money in the account and close it
            return True
        else:
            pass
        
class PremiumAccount(BasicAccount):
    def __init__(self, acName, openingBalance, initialOverdraft): #Defining the initialisers of the premium account
        super().__init__(acName, openingBalance) #here, the premium account claims attributes of the super/parent class basic account
        self.overdraftLimit = initialOverdraft
        if initialOverdraft > 0: #If the overrdraft is less than zero
            self.overdraft = True 
        else: 
            self.overdarft = False
    
    def __str__(self): #Defining the attributes of the premium account as strings
        return f'acName: {self.getName()},cardNum: {self.cardNum}, cardExp: {self.cardExp[0]}/{self.cardExp[1]} ,acNum: {self.getAcNum()} Balance: £{self.getAvailableBalance()}'
    
    #Defining the methods
    def setOverdraftLimit(self, newLimit):
        self.overdraftLimit = newLimit #Designating a new limit for drawing an overdraft from the premium account
        return None

    def getAvailableBalance(self): #Getting the available account balance in there is an overdraft in the account or not
        if self.balance < 0: #if a customer's balance is less than zero or no money in the account.
            self.overdraft = True #if a customer has overdraft benefit.
        else:
            self.overdraft = False #if the customer has no overdraft
        return(self.balance + self.overdraftLimit) #We want to see the balance in the premium account and the overdraft a customer has.
    
    def printBalance(self): #This is going to display/print the amount and the overdraft in the account
        print(f'Balance: £{self.getAvailableBalance()}')
        #print("The amount of overdraft available is" + self.overdraft + "and a remaning overdraft of" +  self.getavailableBalance)
        if self.balance < 0:
            print("You have an overdraft of £{}".format(self.balance))
            return None 
            
    def closeAccount(self): #Closing the account without deleting the account
        if self.balance < 0: #What happens when the balance in the account is less than zero.
            self.overdraft = True #If the bank account has an overdraft
        else:
            self.overdraft = False #if the bank account don't have any overdraftin it.
        
        if self.balance > 0: #What happens when the balance in the account is greater than zero.
            self.withdraw(self.balance) #Withdraw the remaining balance in the account while closing the account
            return True #Sure, the customer is free to take his/her still in the account while closing it.
       
        else:
            print("Can not close account due to customer being overdrawn by £" + str(self.balance)) #If the customer is owing the bank, the account cannot be closed).
            return False #this closing of account cannot happen.
