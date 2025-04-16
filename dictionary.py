thisdict={"brand":"ford","model":"mustang","year":1964}
print(thisdict)
print(type(thisdict))

emp={101:"java",102:"python",103:"c sharpe",104:"java"}
print(emp)
print(emp[101])
print(emp[102])
print(emp[103])
emp[102]="Django"
print(emp)
emp[104]="spring boot"
print(emp)
print(emp[104])


for k in emp:
    print(k)

print("*******************")

for k,v in emp.items():
    print(k,"=",v)


d1=dict(a=10,b=20,c=30)
print(type(d1))

asian={"sonu":50000,"chotu":30000,"boblu":55000}
asian1={"vinu":40000,"sindhu":35000}
print("salary is",asian["sonu"])
print("salary is",asian["chotu"])
print("salary is",asian["boblu"])

del asian["boblu"]
print("asian")



asian["boblu"]=55000
print(asian)
print(asian.items())
print(asian.keys())
print(asian.values())
print(len(asian))
print(max(asian))
print(min(asian))

print("*****************")
print(sorted(asian))
asian1=asian.copy()
print(asian1)
asian2=asian
print(asian2)
print(asian)
print(asian!=asian2)

print("********************")
asian.pop("sonu")
print(asian)
asian.popitem()
print(asian)
asian.clear()
print(asian)

print("************************")
k=[101,102,103]
v=["java","python","Excel"]
d={k:v for (k,v) in zip(k,v)} 
print(d)
print(zip(k,v))

print("*******************")
for k,v in zip(k,v):
    print(k,"=",v)