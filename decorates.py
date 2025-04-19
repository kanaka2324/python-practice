# Example of a higher-order function that takes a function as a parameter


def apply_function(func, value):

   return func(value)

def square(x):
   return x * x

result = apply_function(square, 5)
print(result)


#Another Example of Higher-Order Function:
# Higher-order function returning another function

print("******************")

def outer_function(msg):
  def inner_function():
     print(msg)
  return inner_function

my_func = outer_function("Hello, sonu!")
my_func()


#Function Decorators:
# Example of a decorator


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()

#Without decorater

def result(marks):
   for m in marks:
        if m>=33:
            pass
        else:
            print("Fail")
            break
        else:
            print("pass")

marks =[45,78,18,63,54]
result(marks)

#with decorater

def deco_result(result_fun):
    def distinction(marks):
      for m in marks:
        if m>=75:
           print(m,"Distinction")

result_fun(marks)
return distinction


@deco_result
def result(marks):
    for m in marks:
        if m>=33:
          pass
        else:
           print("Fail")
           break
        else:
           print("pass")

marks =[45,78,18,63,54]
result(marks)