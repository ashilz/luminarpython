from re import *

rule='\w*[@]gmail[.]com'
mailid=input("Enter the email id: ")
matcher=fullmatch(rule,mailid)
if(matcher!=None):
    print("valid email id")
else:
    print("invalid email id")