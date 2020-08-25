lst=[]
lstodd=[]
lsteven=[]
for i in range(1,101):
    lst.append(i)
print(lst)

for i in lst:
    if(i % 2 == 0):
        lsteven.append(i)
    else:
        lstodd.append(i)

print("Even: ",lsteven)
print("Odd: ",lstodd)