f=open("numbers","r")
lst=[]

for num in f:
    lst.append(num.lstrip("\n"))
print(lst)