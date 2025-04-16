s1 = "python,languange"
d="PYTHON"
print(s1.islower())
print(d.isupper())
print(d.lower())
print(s1.upper())

print("************************")

s="Hello,Bharat Bharat"
print(s.replace("Bharat","India"))

print("**************")

s='EduVision education services'
split_list=s.split(' ')
print(split_list)

split_list=['EduVision','education','services']
print("".join(split_list))

print("*******************")
d="123456"
print(d.isdigit())

s2="python"
print(s1==s2)

print(ord('p'))
print(ord('P'))
print(s1<=s2)
print(s1!=s2)
print(s1[0])
print(s1.index('languange'))
print(s1.count('a'))
print(s1.startswith('python'))
print(s1.endswith('languange'))
print(s1.split(','))


print("************")
d=['python languange']
print(",".join(d))
n="Hello.{}"
print(n.format("sonu"))
print("{},how are you?".format("sonu"))
print("{},{},{}".format("one",25,3.5))
print("{2},{0},{1}".format("one",25,3.5))

s1="35,40,20,10,55,80,17,60"
print(s1)
di=s1.split(",")
print(di)

x=[int(i)for i in di]
print(x)

list_of_str=["25","12","2022"]
all_str="".join(list_of_str)
print(all_str)

date_str="-".join(list_of_str)
print(date_str)

A=[2,45,43,22,34,56,72]
data=[]
for num in A:
    if num%2==0:
        data.append(num)
print("even num is",data)

print(type(s1))

print("*************")
#s={10,20,30,"iiht",10+6j,10,20,3.14}
#print(s)

s={100,20,30,40,50}
print(s)
print(len(s))
print(max(s))
print(min(s))
print(sorted(s))

print("**************") 

for i in s:
    print(i,end=" ")

print("************") 

s.add("python")
print(s) 
b=s.copy()
print(b)

print("*******************")
s.remove(40)
print(s)

print("***************")
s.update([56,89,36])
s.update("rajeev")
print(s)

s.clear()
print(s)

print(type(s))

print("**************")
v=set()
v.update([2,3,4])
print(v)

s={10,20,30,5,6}
print(s)
s.add("python")
print(s)

s.clear()
print(s)
s.add("java")
print(s)

c=s.copy()
print(c)
print(c==s)

print("**************")
a1={"java","python","c#","excel"}
a2={"vs code","eclipse","java","advance java"}

d=a1.difference(a2)
print(d)

a1.difference_update(a2)
print(a1)

a1.discard("c#")
print(a1)

print("***************")
a1.add("vs code")
print("a1=",a1)
print("a2=",a2)

i=a1.intersection(a2)
print(i)

a1.intersection_update(a2)
print(a1)  

print("**************")
s1={10,20,30,40}
s2={10,20,30,40}


z=s1.isdisjoint(s2)
print(z)

z=s1.issubset(s2)
print(z)

print("*********")

num=[10,20,31,40,51,60,85,80]

e={x for x in num if x%2==0}
print(e)