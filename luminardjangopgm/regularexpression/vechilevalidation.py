#vechile validation
from re import *
rule='[Kk][Ll][0-9]{2}[a-z]{1,2}\d{4}'

regno=input("enter vechile reg num: ")
matcher=fullmatch(rule,regno)
if(matcher!=None):
    print("valid reg no")
else:
    print("invalid regno")