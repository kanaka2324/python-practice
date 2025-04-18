#polymorphism -----the occurrence of something in multiple forms

#method overloading-----not supported to python
#method overriding


#method overriding

class Animal:
    def make_sound(self):
         print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
         print("Woof!")

class Cat(Animal):
    def make_sound(self):
         print("Meow!")

animals = [Dog(), Cat(), Animal()]
for animal in animals:
     animal.make_sound()



 # operator overloading  

class ComplexNumber:
     def __init__(self, real, imag):
         self.real = real
         self.imag = imag

     def __add__(self, other):
         return ComplexNumber(self.real + other.real, self.imag + other.imag)

num1 = ComplexNumber(5, 3)
num2 = ComplexNumber(2, 1)
result = num1 + num2
print(result.real, result.imag)


#method overloading
 
#same name,different parameter

def product(a,b):
    p=a*b
    print(p)

def product(a,b,c):
    p=a*b*c
    print(p)

#product(4,5)
product(1,2,3)