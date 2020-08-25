class Person:
    def setValues(self,pname,age):
        self.pname=pname
        self.age=age

    def printValues(self):
        print(self.pname)
        print(self.age)

class Bank(Person):
    bname="SBK"
    def __init__(self,accno,pname):
        self.accno=accno
        self.pname=pname
        self.balance=3000

    def printValues(self):
        print("Account Number: ",self.accno)
        print("Name          : ",self.pname)

    def deposit(self,amount):
        self.balance+=amount
        print("Your",Bank.bname,"has been credited with amount of ",amount)

    def withdraw(self,amount):

        if(amount>self.balance):
            print("Transaction has been cancelled")
        else:
            self.balance-=amount
            print("Your ",Bank.bname," has been debited with ",amount)

    def BalanceEnquiry(self):

        print("Your currnent available balance", self.balance)



obj = Bank(83338, "Aswathy Ashil")
obj.deposit(5000)
obj.withdraw(2000)
obj.BalanceEnquiry()
obj.printValues()



