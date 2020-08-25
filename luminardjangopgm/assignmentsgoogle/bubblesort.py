lst=[10,100,20,3,9.52,66]
lst1=len(lst)

for i in range(lst1-1):
    if lst1[i]>lst1[i+1]:
        lst1[i],lst1[i+1] = lst1[i+1],lst1[i]

print("Sorted List: ",lst1)