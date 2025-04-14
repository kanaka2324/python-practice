a = int(input("enter number a :"))

b = int(input("enter number b :"))

sum= a + b
sub = a - b 
mul = a * b
div = a/b
fld = a//b
rem = a % b
print("Sum of a and b is :",sum)
print("Sub of a and b is :",sub)
print("Mul of a and b is :",mul)
print("Div of a and b is :",div)
print("f Div of a and b is :",fld)
print("rem of a and b is :",rem)
print("**************************************")  

a = int(input("enter number a :"))

b = int(input("enter number b :"))
print("output is :",a>b)
print("output is :",a<b)
print("output is :",a>=b)
print("output is :",a<=b)
print("output is :",a!=b)
print("output is :",a==b)
print("**************************************")



print("Statment is :",a>b and a<b)
print("Statment is :",a>b or a<b)
print("Statment is :",not(a>b and a<b))
print("**************************************")



c = 30
c +=10 # c =  c + 10
print("Answer is ",c)
c-=2
print("Answer is ",c)
c//=2
print("Answer is ",c)
c%=3
print("Answer is ",c)
c*=30
print("Answer is ",c)


print("**********************")
a = 10
b = 20
print("output is ",a&b)
print("output is ",a|b)
print("output is ",a^b)
print("output is ",~b)
print("output is :",~a)