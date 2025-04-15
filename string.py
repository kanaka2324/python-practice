x = "Hello"
print(type(x))

print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print("**************************")
print(x[-1])
print(x[-2])
print(x[-3])
print(x[-4])
print(x[-5])

print("**************************")

n = len(x)
print("Size of x is",n)



for i in range(len(x)):
    print(i,x[i])

print("**************************")


for i in x:
    print(i)

print("**************************")


i = 0
while i<len(x):
    print(i,x[i])
    i+=1
print("**************************")


greeting = "hello goodmorning"
print(greeting[:])
print(greeting[0:])
print(greeting[1:5])
print(greeting[1::2])
print(greeting[::-1])
print(greeting[-1::-3])