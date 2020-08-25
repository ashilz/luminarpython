lower=int(input("enter the lower limit: "))
upper=int(input("enter the upper limit: "))


for i in range (lower,(upper+1)):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if (flag==0):
        print(i)
