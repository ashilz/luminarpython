f=open("numbers","r")
lst=[]
res=0
for num in f:
    lst.append (int(num))
#res=sum(int(lst))
print(lst)
res=sum(lst)
print(res)