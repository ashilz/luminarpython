#parent Super Base
#child  sub   dervied


#single imheritance
class Parent():
    def phone(self):
        print("Have samsung galaxy A6")

class child(Parent):
    pass


c=child()
c.phone()