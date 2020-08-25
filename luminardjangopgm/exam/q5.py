lst=[1,2,3,4]
element=int(input("Enter the num:"))
low=0
upp=len(lst)-1
lst.sort()
while(low<=upp):
    data=lst[low]+lst[upp]
    if(data==element):
        print(lst[low],",",lst[upp])
        break
    elif(data>element):
        upp=upp-1
    else:
        low=low+1
print(lst)