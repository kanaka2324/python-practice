#global variables
x = 10 # Global variable
def display():
   print(x) # Accessing global variable
display()



#local variable
def display():
  y = 5 # Local variable
  print(y)
display()

#instance object variable

class Person:
   def __init__(self, name):
       self.name = name # Instance object variable

p1 = Person("sonu")
p2 = Person("chotu")
print(p1.name)
print(p2.name)


#class object variable
class Student:
   school = "ABC School" # Class object variable
   def __init__(self, name):
       self.name = name

s1 = Student("Ravi")
s2 = Student("Sita")
print(s1.school)
print(s2.school)
# Modify class variable
Student.school = "XYZ School"
print(s1.school)
print(s2.school)