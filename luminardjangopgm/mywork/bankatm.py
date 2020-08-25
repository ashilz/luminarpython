print("Welcome to New Bank of Ashilz ATM")
restart=("Y")
chances=3
balance=300
while chances>=0:
    pin=int(input("Please enter the 4 digit pin: "))
    if pin==(1234):
        print("You entered your pin correctly\n")
        while restart not in ('n','NO','no','no'):
            print("Please press 1 for Balance\n")
            print("Please press 2 to make a Withdrowl\n")
            print("Please press 3 to Pay in\n")
            print("Please press 4 to Return Card\n")
            option=int(input("What would you like to choose?"))
            if option==1:
                print("Your Balance is :",balance,'\n')
                restart=input("Would you like to go back?")
                if restart in ('n','NO','no','no'):
                    print("Thank you")
                    break
            elif option==2:
                option2=('Y')
                withdrawl=float(input("How much would you like to withdraw?"))
                if withdrawl in [10,20,40,60,80,100]:
                    balance=balance-withdrawl
                    print("Your Available Balance is ",balance)
                    restart=input("Would you like to go back?")
                    if restart in ('n','NO','no','no'):
                        print("Thank You")
                        break
                elif withdrawl!=[10,20,40,60,80,100]:
                    print("Invalid Amount, Please Try again\n")
                    restart=('y')
                elif withdrawl==1:
                    withdrawl=float(input("Please enter the desired amount:"))