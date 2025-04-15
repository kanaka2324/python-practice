s = "hellopython"
print(max(s))
print(min(s))


print(sorted(s))

print(ord('h'))
print(chr(104))


for i in range(len(s)):
     print(i,s[i],ord(s[i]))

s = "12345"
print(type(s))
print(sum(int(x) for x in s)) 


s1 = "Hello"
s2 = "World"
result = s1 + " " + s2 
print(result) 

s1 = "Hello "
s2 = "World"
s3 = s1 + s2 
print(s3) 


s = "hello "
result = s * 3
print(result) 


s1 = "Namaskara"
s2 = "Namaskara"
print(s1 == s2) 

s1 = "Namaste"
s2 = "Bharat"
print(s1 != s2) 



s1 = "apple"
s2 = "Apple"
print(s1 > s2)


s1 = "Apple"
s2 = "apple"
print(s1 > s2)

#index()
s = "Hello, Bharat"
print(s.index("Bharat")) 

s = "Hello, Bharat"
print(s.index(" ")) 

#count()
print(s.count('a'))

s="Hello,Bharat"
print(s.startswith('Hello'))
print(s.endswith('Bharat'))
print(s.split(','))


words = ["Hello", "Bharat"]
print(",".join(words))


s = "Hello, {}"
print(s.format("python")) 

s = "12345"
print(s.isdigit()) 

s = "hello"
print(s.islower()) 

s = "Hello, Bharat"
print(s.lower()) 

s="HELLO"
print(s.isupper())

s="Hello,Bharat"
print(s.upper())

s = "Hello, Bharat"
print(s.replace("Bharat", "India")) 


s = 'EduVision education services'
split_list=s.split(' ')
print(split_list)


Li = [
  "EduVision"
  "education",
  "services"
 ]

space='   '
s2 = space.join(Li)
print(s2)

print("{}, how are you?".format("sonu"))


print("{}, {}, {}".format("one", 25, 3.5))
print("{2}, {0}, {1}".format(10, 20, 30))

print("*********************")
S1 = "35, 40, 20, 10, 55, 80, 17, 60"
di = S1.split(",")
print(di)


mylist = [int(e) for e in di]
print(mylist)


list_of_str = ["25", "12", "2022"]
# Joining the list into a single string with no separator
all_str = "/".join(list_of_str)
# Output the result
print(all_str)