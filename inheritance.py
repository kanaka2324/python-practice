"""
#single level inheritance

class A:
    def showA(self):
        print("a class method")
class B(A):
    def showB(self):
        print("b class method")



a  = A()
a.showA()
print("-----------------------------")
b = B()
b.showB()
b.showA()


#multi level inheritance

class A:
    def showA(self):
        print("a class method")
class B(A):
    def showB(self):
        print("b class method")
class C(B):
    def showC(self):
        print("c class method")


a  = A()
a.showA()
print("-----------------------------")
b = B()
b.showB()
b.showA()
print("-----------------------------")
c = C()
c.showA()
c.showB()
c.showC()


# Hierarchical ----
print("***********************")
class A:
    def showA(self):
        print("a class method")
class B(A):
    def showB(self):
        print("b class method")
class C(A):
    def showC(self):
        print("c class method")


a  = A()
a.showA()
print("-----------------------------")
b = B()
b.showB()
b.showA()
print("-----------------------------")
c = C()
c.showA()
c.showC()

# Multiple 

print("**********************")
class A:
    def __init__(self):
        print("a class constructor")
    def showA(self):
        print("a class method")
class B:
    def __init__(self):
        print("b class constructor")
    def showB(self):
        print("b class method")
class C(B,A):
   
    def showC(self):
        print("c class method")


a  = A()
a.showA()
print("-----------------------------")
b = B()
b.showB()

print("-----------------------------")
c = C()
c.showA()
c.showB()
c.showC()
"""
#hybride----
print("********************")

class A:
    def showA(self):
        print("a class method")

class B:
    def showB(self):
        print("b class method")

class C(B,A):
    def showC(self):
        print("c class method")

class D(C):
    def showD(self):
        print("d class method")

class E(C):
    def showE(self):
        print("e class method")

print("********************")
a=A()
a.showA()
print("********************")
b=B()
b.showB()
print("********************")
c=C()
c.showA()
c.showB()
c.showC()
print("********************")
d=D()
d.showC()
d.showD()
print("********************")
e=E()
e.showC()
e.showE()



