lst=[10,12,13,14,15]
cnt=len(lst)

p=1

for i in range(0,cnt):
    res=lst[i]**p
    p+=1
    print(res)
