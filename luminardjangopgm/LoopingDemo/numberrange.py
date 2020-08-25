#print number b\w low to uper

low=int(input("enter low: "))
upp=int(input("enter upper limit: "))


evensum=0
oddsum=0
for i in range(low,(upp+1)):
    if(i%2==0):
        evensum+=1
    else:
        oddsum+=oddsum
        print(i)



print("sum of even numbers: ",evensum)
print("sum of odd numbers: ",oddsum)