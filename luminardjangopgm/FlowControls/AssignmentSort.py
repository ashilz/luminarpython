#sorting

num1=int(input("enter num1: "))#
num2=int(input("enter num2: "))#
num3=int(input("enter num3: "))#

if(num1<num2):
    temp=num1
    num1=num2
    num2=temp

if(num1<num3):
    temp=num1
    num1=num3
    num3=temp

if(num2<num3):
    temp=num2
    num2=num3
    num3=temp
print("after sorting")
print(num1,num2,num3)