
num=int(input("enter the number: "))#235

res=0

while(num!=0):#235
    #we have to fetch last digit
    digit=num%10#235/10=23.5
    res=(res*10)+digit#
    num=num//10
print(res)