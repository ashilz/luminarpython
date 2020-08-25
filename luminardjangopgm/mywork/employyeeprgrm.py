from functools import *
class Employee:
    def __init__(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=int(salary)

    def printEmp(self):
        print("Name: ",self.name)
        print("Designation: ",self.desig)

    def __str__(self):
        return self.name

f=open("Emplfile","r")
lst=[]
for data in f:
    values=data.rstrip("\n").split(",")
    #print(values)
    id=values[0]
    name=values[1]
    desig=values[2]
    salary=values[3]
    obj=Employee(id,name,desig,salary)
    obj.printEmp()
    #print(obj)
    lst.append(obj)

#for emp in lst:
#    print(emp)
#maxsal=reduce(lambda sal1,sal2:sal1 if sal1>sal2)

upper=list(map(lambda obj:obj.name.upper(),lst))
print(upper)

salary_inc=list(map(lambda obj:obj.salary+5000,lst))
print(salary_inc)
#max_sal=list(filter(lambda obj:int(obj.salary)>50000,lst))

#for lst in max_sal:
#    print(lst)

#high_salary=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,list(map(lambda emp:emp.salary,lst)))
#print("Highest Sal=",high_salary)
#high_sal=list(map(lambda obj:obj.salary,lst))
#print(high_sal)

maxx_sal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,salary_inc)
print("Highest Salary:",maxx_sal)

maxsalemp=lst(filter(lambda emp:emp.emp.salary==maxx_sal,salary_inc))
print(maxsalemp)