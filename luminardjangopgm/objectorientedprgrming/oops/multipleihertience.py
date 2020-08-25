class Parent:
    def m1(self):
        print("inside parent1")

class Child:

    def m2(self):
        print("inside child1")

class SubChild(Child,Parent):
    def m3(self):
        print("Inside subchild")

s=SubChild()
s.m3()
s.m2()
s.m1()