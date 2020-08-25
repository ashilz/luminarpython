#exception keyword

#try:
#   doubtful code
#except:
#   handling code
#finally:
#   cleanupcode


num1=int(input("enter value for num1:"))
num2=int(input("enter value for num2:"))

lst=[1,2,3,4]

try:
    res=num1/num2
#it is an abnormal code or casee which terminate the normal flow of the program
    print("result=",res)
    pos=int(input("enter index postion"))
    print(lst[pos])
    print("we have database transaction")
    print("file operation")
    print("process completed sucessfully")
except Exception as e:
    print(e.args)

