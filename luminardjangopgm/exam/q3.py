num=int(input("Enter the number to divide: "))#10
div=int(input("Enter the number: "))#3


quo=0
               #0,10
while(num>=div):
    num=num-div
    quo+=1
print("Remider: ",num)
print("Quotient: ",quo)