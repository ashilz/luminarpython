#program to find factoraial of the given number

def factNum():
    num=int(input("enter num: "))
    fact=1
    for i in range(1,(num+1)):
        fact=fact*i
        print(fact)
factNum()

def fact(num):
    res=1
    for i in range(1,(num+1)):
        fact=fact*i
        return res


