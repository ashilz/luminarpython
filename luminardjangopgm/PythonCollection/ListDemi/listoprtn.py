#3,5,8=13,11,8
#2,4,6=10,8,6

lst=[2,4,6]
ls=[]
f=0
for i in lst:
    index=lst.index(i)
    if(index==0):
        f=lst[1]+lst[2]
        ls.append(f)
    elif(index==1):
        f=lst[0]+lst[2]
        ls.append(f)
    elif(index==2):
        f=lst[0]+lst[1]
        ls.append(f)
    else:
        break
print(lst," = ",ls)
