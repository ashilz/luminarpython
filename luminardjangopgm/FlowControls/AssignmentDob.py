#dob

dd=int(input("Enter the dob date: "))
dm=int(input("Enter the dob month: "))
dy=int(input("Enter the dob year: "))

print("DOB:",dd,"-",dm,"-",dy)

cd=int(input("Enter the current date: "))
cm=int(input("Enter the current month: "))
cy=int(input("Enter the current year: "))

age=(cy-dy)-1
age1=dm-cm
age2=cm-dm
age3=cy-dy

if(age<=1) & (cm<dm):
    age1 = ((12-dm)+cm)
    print(age1,"months older baby")
elif(age>=1) & (cm<dm):
    age1 = ((12-dm)+cm)
    print("Age is: ",age,"year and ",age1,"months older")
elif((age>=1) & (cm>dm)):
    print("Age is: ",age3,"year and ",age2,"months older")
else:
    print("Age is: ",age,"years old")
