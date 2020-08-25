#def add(num1,num2):
#    return num1+num2
#variable length arg method

#def printVal(name,loction):
#    print(name)
#   print(loction)

#printVal("ajay","kakkanad","aluve")



def add (**args):
    print(args)
    res=0
    for k,v in args.items():
        res+=v
    print("res=",res)

add(num1=10,num2=20,num3=40)

#this will excute in dict format
#key value pair