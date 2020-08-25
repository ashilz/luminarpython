class Employee():

#init is the consructor name

    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desg=desig
        self.salary=salary

    def printvalues(self):
        print(self.eid)
        print(self.ename)
        print(self.desg)
        print(self.salary)


#constructor automatically ivokes

obj1=Employee(1001,"rahul","ceo",50000)
obj1.printvalues()