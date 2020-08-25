from re import *
lst=[]
rule='[Kk][Ll][0-9]{2}[a,z]{2}\d{4}'
f=open("regno","r")
for line in f:
    data=line.rstrip("\n")
    matcher=fullmatch(rule,data)
    if(matcher!=None):
#        print("valid")
        lst.append(data)
    else:
        pass
print("valid reg no",lst)

#f1=open("regno","w")
#for item in lst:
#    f1.write("%s\n"%item)#line by line output
#    f1.write(item)
#f1=open("regno1","r")
#print("output file:")
#for data in f1:
#    print(data)