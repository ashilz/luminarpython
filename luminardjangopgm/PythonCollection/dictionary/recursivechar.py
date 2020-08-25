pattern="ABABAC"
rec={}
#first recursive charctor

for char in pattern:
    if(char not in dict):
        rec[char]=1
    else:
        print("first recursive charactor=",char)
        break

