num=int(input("Enter a Number: "))#6
flag=0
for i in range(2,num): #2-6
    if(num%i==0):#6%2=0
        flag=1
        break
    else:
        flag=0

if(flag>0): #1>0
    print("Input number is Not Prime")#this statement will print
else:
    print("Input number is Prime")