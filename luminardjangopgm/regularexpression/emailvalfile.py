from re import *
lst=[]
rule='\w*[@]gmail[.]com'
f=open("emailval","r")
for line in f:
    data=line.rstrip("\n")
    matcher=fullmatch(rule,data)
    if(matcher!=None):
        lst.append(data)
    else:
        pass

print(lst)

f1=open("emailval","w")
for item in lst:
    f1.write("%s\n"%item)
    f1.write(item)
f1=open("regno1","r")
print("output file:")
for data in f1:
    print(data)

print(lst)