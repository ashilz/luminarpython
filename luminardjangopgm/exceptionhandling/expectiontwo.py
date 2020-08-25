num1=int(input("enter value for num1:"))
num2=int(input("enter value for num2:"))

lst=[1,2,3,4]

try:
    res=num1/num2
#it is an abnormal code or casee which terminate the normal flow of the program
    print("result=",res)
except Exception as e:
    print(e.args)
finally:
    print("we have database transaction")
    print("file operation")
    print("process completed sucessfully")
except Exception as e:
    print(e.args)

   pos=int(input("enter index postion"))
    print(lst[pos])