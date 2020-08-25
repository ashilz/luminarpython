#import FunctionProgram.operations
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
#sum=FunctionProgram.operations.add(num1,num2)
#print(sum)

from FunctionProgram.operations import *
sum=add(num1,num2)
print("Answer is=",sum)
