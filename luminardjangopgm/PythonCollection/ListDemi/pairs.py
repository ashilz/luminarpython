#interview question
lst=[1,2,3,4]

element=int(input("enter value: "))
lst.sort()

low=0
upp=len(lst)-1

while(low<=upp):#0<=3
    data=lst[low]+lst[upp]#0+3

    if(data==element):#3==4
        print("pairs",lst[low],",",lst[upp])
        break
    elif(data>element):
        upp=upp-1
    else:
        low=low+1
