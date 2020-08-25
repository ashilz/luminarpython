string="ABABABCAAA"
dict={}
for i in string:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
ans=max(dict,key=dict.get)
print(ans)