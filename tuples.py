t = (10,3.64,10+6j,False,10,80,90,20,60)
print(t[0:])
print(t[1:])
print(t[1:5])
print(t[:5])
print(t[:-3])

print(t[3::2])

t1=(2,3,4)
print(t+t1)

t1=t
print(t)
print(t1)

print(type(t))
print(t)



print(type(t)) 
print(t)


print("size of tuple :",len(t))



t = (10,3.64,10+6j,False,10,80,90,20,60)
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print("================================")
print(t[-1])
print(t[-2])
print(t[-3])
print(t[-4])
print("================================")



for i in t:
    print(i,end=" ")
print()
print("================================")

for i in range(len(t)):
     print("index is",i,":",t[i])


print("================================")

i = 0
while i<len(t):
     print("index is",i,":",t[i])
     i+=1

print("================================")    



print("index of 10 is ",t.index(10))
print("count of 10 is ",t.count(10))



data=(10,210,300,40)
print(sorted( data))

data=list(data)


 