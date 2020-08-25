#validateall mobile number

from re import *

rule='\d{10}'
mobileno=input("Enter the mobile number: ")
matcher=fullmatch(rule,mobileno)
if(matcher!=None):
    print("valid mobile number")
else:
    print("Invalid mob number")
