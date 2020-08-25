num = int(input("enter the number: "))#3

a=0
if num % 2 == 0:#
    a=(num/2) *(num+1)
else:
    a=((num+1)/2)*num
print(a*a)

res=0

while(rev!=0):
    digit=rev%10
    res=(res*10)+digit
    rev=rev//10
print(res)


