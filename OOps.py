class A:
    x = 10
    
    def showA(self):
        print("i am in class A")

a = A()
a.showA()
a.x = 20
print(a.x)


class Animal:
    name="sonu"
    age="24"
    color="chocalate"

    def showDetails(self):
        print("Animal name is:",self.name)
        print("Animal age is:",self.age)
        print("Animal color is:",self.color)

a=Animal()
a.showDetails()


class Vehicle:
    brand = "Thar"
    start = "self start"
    price = "400000"

    def brandDetails(self):
        print(self.brand)
        print(self.price)
        print(self.start)


t =  Vehicle()
t.brandDetails()





class Trainer:

    start_date = 6
    start_month =1
    end_month = 2
    start_year = 2025
    def __init__(self,name,sub):
      self.name = name
      self.sub = sub

    def session(self):
        print("starting session :",end="")
        print(self.start_date,self.start_month,self.start_year,sep="/")
        print("Ending session :",end="")
        print(self.start_date,self. end_month,self.start_year,sep="/")

        print("Trainer Name:",self.name)
        print("Technology :",self.sub)


t = Trainer("Rajeev","python")
t.session()


