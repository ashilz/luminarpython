#lst=[]

#for i in range(50,100):
 #   lst.append(i)

#print(lst)


oddlst=[]
evenlst=[]
lst=[]

for i in range(1,100):
    lst.append(i)
print(lst)

for i in lst:
    if(i%2==0):
        evenlst.append(i)
    else:
        oddlst.append(i)
print("odd",oddlst)
print("even",evenlst)
