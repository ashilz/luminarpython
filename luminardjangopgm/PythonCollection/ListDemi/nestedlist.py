employes=[[1001,"ashil",15000],
     [1002,"rinson",20000],
     [1003,"vinu",17000],
     [1004,"binu",25000]]

sum=0
#for emp in employes:
    #print(emp)
    #print(emp[1])

#print emp name  who have salary>17000
for emp2 in employes:
    if(emp2[2]>17000):
        print(emp2[1])

#sum of sal
for emp3 in employes:
    sum=sum+emp3[2]
print(sum)