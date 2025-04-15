l = [100,10.36,True,3+6j,"python"]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print("*****************************")
print(l[-1])
print(l[-2])
print(l[-3])
print(l[-4])
print(l[-5])

print("Before any change list item is :",l)
l[2] = "Data analyst and full stack"
print("After changing  list item is :",l)
print("*****************************")



for i in l:
    print(i)
print("*****************************")


s = len(l)
print("size of the list ",s)
print("*****************************")

for i in range(len(l)):
    print("index of",i,"is",l[i])
print("******************************")


i = 0
while i<len(l):
    print("index of",i,"is",l[i])
    i = i +1


print("******************************")
print("before we apply any function list is  :",l)
l.append("Excel")



print("*****************************")

print("before we apply any function list is  :",l)
l.append("Excel")
print("Appended Data list is :",l)
l.remove(3+6j)
print("removed Data list is :",l)
l.insert(100,"NoSQL")
print("1ST index Data list is :",l)

print("*****************************")

l.append("Excel")
print("Appended Data list is :",l)

print("*****************************")
l.reverse()
print("reversed Data is ",l)


print("*****************************")
item = l
print("copy data is",item)




print("*****************************")
del l[1]
print("After Deletion Data of list is ",l)


print("*******************************")
deleteddata = l.pop()
print("After deletion Data list item is ",l)
print("Deletd Data of list is--->",deleteddata)

print("**********************************")
data=[200,300,5,2,8,900.69]
print(sorted(data))

print("after sort data list is",data)


storename =["apple","banana","orange","kivi"] 
print(storename)

print(sorted(storename))
print("******************")
storename.sort()
  



l = [100,10.36,True,3+6j,"python"]
l1=[6,7,8]
print(sum(l1))
print(max(l1))
print(min(l1))

print(type(l))