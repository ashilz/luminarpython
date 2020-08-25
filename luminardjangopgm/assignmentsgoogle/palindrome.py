#sequence is a Palindrome or not
num=int(input("Enter the Sequence:"))#3212

string=str(num) #converting int number to string
rev_num=string[::-1]#2123

if(string==rev_num):#3212==2123
    print("Entered sequence is Palindrome")
else:
    print("Entered sequence is Not Palindrome")#this statement will print

