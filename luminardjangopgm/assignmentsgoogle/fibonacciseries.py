#fibonacciseries

limit=int(input("Enter the limit: "))#5

num1=0
num2=1

for i in range(limit):#i=0 i=1 i=2 i=3,i=4
    print(num1) #0,num1=0,num1=1,num1=2,num=3
    temp=num1 #temp=0,temp=1,temp=2
    num1=num2 #numm1=1,1,num=1,
    num2=temp+num2#num2=0+1,1+1,2+1

