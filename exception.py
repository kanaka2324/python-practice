#a = int(input("Enter a number: "))

#IndexError

#my_list = [1, 2, 3]
#print(my_list[5])

#AttributeError

#my_list = [1, 2, 3]
#my_list.append(4)
#my_list.push(5)

#a = 10
#b = 0
#result = a / b

#keyError
#my_dict = {'name': 'Rajeev', 'age': 27}
#print(my_dict['address'])


#NameError
#print(age)

#typeError
#a = '10'
#b = 5
#result = a + b
#print("result")


#built-in exception
#import builtins
#print(dir(builtins))

#for x in locals()['__builtins__']:
 #  print(x)


#user defined

class InsufficientBalance(Exception):
    def __init__(self, errormsg):
        self.errormsg =errormsg
    def __str__(self):
        return self.errormsg

class Account:
    def __init__(self,accno,bal):
        self.accno =  accno
        self.balance = bal
    
    def showBalance(self):
        print("Your Current balance is ",self.balance)
    
    def withrow(self,amt):
        if self.balance <amt:
            raise InsufficientBalance("Insufficient Funds")
        self.balance = self.balance - amt
        print("You have withdrown,",amt)


my_acount = Account(100,5000)
my_acount.showBalance()
try:
    my_acount.withrow(8000)
except InsufficientBalance as e:
    print(e)
my_acount.showBalance()





try:
    a = int(input("Enter a number "))
    b = int(input("Enter another number "))
    if b==0:
        raise ZeroDivisionError("Cant Devide by a number b")
    c = a/b
    print(c)
except Exception as e:
    print(e)

print("program still continue")
