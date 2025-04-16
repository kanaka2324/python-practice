#Non-Keyword Arguments (Positional Arguments)

def greet(name, age):
    print("Name:", name)
    print("Age:", age)
        
# Calling the function with positional arguments
greet("sonu", 24)
greet("kanu",20)

#Keyword Arguments

def greet(name, age):
    print("Name:", name)
    print("Age:", age)

# Calling the function with keyword arguments
greet(name="vinu", age=20)
# Keyword arguments allow you to specify arguments in any order
greet(age=20, name="sindhu")


#Combining Non-Keyword and Keyword Arguments
def describe_person(name, age, city):
    print("Name:", name)
    print("Age:", age)  
    print("City:", city)

# Combining positional and keyword arguments
describe_person("Shubhan", age=26, city="Madhubani")


#Summary
#Non-Keyword (Positional) Arguments: The order in which arguments are passed matters.

def example(a, b):
    print("a:", a)
    print("b:", b)

example(1, 2)

#Keyword Arguments: The order does not matter because each argument is explicitly named.

def example(a, b):
    print("a:", a)
    print("b:", b)
example(b=2, a=1)


#*args(non-keyword arguments)

def my_function(*args):
   for arg in args:
        print(arg)

# Calling the function with multiple arguments
my_function(1, 2, 3, "Hello", "Shubhan")


#**kwargs (Keyword Arguments)

def my_function(**kwargs):
   for key, value in kwargs.items():
      print(key, ":", value)

# Calling the function with multiple keyword arguments
my_function(name="Shubhan", age=26, city="Madhubani")


#Combining *args and **kwargs

def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling the function with both positional and keyword arguments
my_function(1, 2, 3, name="Shubhan", age=26)






