class Employee():

    def setEmployee(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desg=desig
        self.salary=salary


#instance variable=self.ename,eid
#eid,ename are local variables
#self is a key word used to point current  class instance 

    def printvalues(self):
        print(self.eid)
        print(self.ename)
        print(self.desg)
        print(self.salary)

obj1=Employee()
obj1.setEmployee(1001,"rahul","ceo",50000)
obj1.printvalues()