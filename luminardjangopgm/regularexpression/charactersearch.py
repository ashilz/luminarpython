from re import *

#pattern='[abc]' check either a,b or c
#pattern='[a-z]'#this will check ch for lower case a to z
#pattern='[A-Z]'#check upper case
#pattern='[a-zA-Z]'#check upper and lower [0-9][A-z]
#pattern='[^a-zA-Z0-9]'#'^' expect precial char


#predefined charcter

#pattern="\s" #it will check for spaces
#pattern ="\d" #it will check for digit[0-9]
#pattern='\D'#[^0-9]
#pattern="\w"#check for all words(lower,upper and digit)
pattern="\W"#expect, so it will print all special char in the string
matcher=finditer(pattern,"ab&xP 72xyZ@cz#")#finditer returns in the form of list and set

for match in matcher:
    print(match.start()) #postion of the match found
    print(match.group())#returns the object match