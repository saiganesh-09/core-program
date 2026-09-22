'''
Python Magic Methods
Question 1: Bank Account Operations
Create a class BankAccount with:
•	attributes: account_holder, balance
•	instance method: deposit(amount)
•	instance method: withdraw(amount)
Implement these magic methods:a
•	__str__() → display account details
•	__add__() → add balances of two accounts
•	__sub__() → subtract balances
•	__eq__() → compare if two accounts have same balance
•	__lt__() → check which account has lower balance
•	__getattribute__() → print a message whenever an attribute is accessed
•	__setattr__() → prevent setting negative balance
Demonstrate creating two accounts and using all operations.'''
# class BankAccount:
#     def __init__(self,account_holder,acc_num,balance=0):
#         self.name=account_holder
#         self.acc_num=acc_num
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         return self.balance
#     def withdraw(self,amount):
#         self.balance-=amount
#         return self.withdraw
#     def __str__(self):
#         return f"Account_holder:{self.name}\nAccount_Number:{self.acc_num}\nBalance:{self.balance}"
#     def __add__(self, other):
#         return self.balance+other.balance
#     def __sub__(self, other):
#         if self.balance>other.balance:
#             return self.balance-other.balance
#         else:
#             return other.balance-self.balance
#     def __eq__(self, other):
#         return self.balance==other.balance
#     def __lt__(self, other):
#         if self.balance<other.balance:
#             return f"{c1.name} has less amount"
#         else:
#             return f"{c2.name} has less amount"
# c1=BankAccount("sai",12345,67889)
# c2=BankAccount("aditya",67890,123454)
# # print(c1)
# # print(c2)
# print(c1.deposit(5000))
# print(c2.deposit(6000))
# c1.withdraw(500)
# c2.withdraw(600)
# # print(c1)
# # print(c2)
# print(c1==c2)
# print(c1<c2)

from statistics import quantiles

'''
Question 2: Product Price Comparison
Create a class Product with:
•	attributes: name, price, quantity 
•	method: total_price() 
Implement:
•	__str__() 
•	__add__() → add total prices of two products 
•	__mul__() → multiply product price by a number 
•	__gt__() → compare which product has greater total value 
•	__eq__() → compare prices 
•	__getattr__() → return "Attribute not found" for missing attributes 
•	__setattr__() → do not allow price less than 0 '''
# class Product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def total(self):
#         return self.price*self.quantity
#     def __str__(self):
#         return f'Product Name:{self.name}\nPrice:{self.price}\nQuantity:{self.quantity}\nTotal:{self.total()}'
#     def __add__(self, other):
#         return self.total()+other.total()
#     def __mul__(self, number):
#         return self.price*number
#     def __gt__(self, other):
#         if self.total()>other.total():
#             return f'{self.name} has greater total value'
#         else:
#             return f'{other.name} has greater total value'
#     def __eq__(self, other):
#         return self.price==other.price
#     def __getattr__(self, attribute):
#         return "Attributes not found"
#     def __setattr__(self, key, value):
#         if key=="price" and value <0:
#             print('Price cannot be less than 0')
#         else:
#             object.__setattr__(self,key,value)
# p1=Product("laptop",55678,2)
# p2=Product("Mobile",25578,2)
# print("Total price of p1:",p1.total())
# print("Total price of p2:",p2.total())
# print('Addition:',p1+p2)
# print("Multiplication:",p1*3)
# print(p1>p2)
# print("Price equal:",p1==p2)

'''Question 3: Student Marks
Create a class Student with:
•	attributes: name, marks 
•	method: grade() 
Implement:
•	__str__() 
•	__add__() → add marks of two students 
•	__truediv__() → divide marks by a number 
•	__ge__() → check if one student scored greater than or equal to another 
•	__lt__() → check if one student scored less 
•	__getattribute__() → track attribute access 
•	__setattr__() → marks must be between 0 and 100 '''
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def grade(self):
#         if self.marks>=90:
#             return 'A'
#         elif self.marks>=80:
#             return 'B'
#         elif self.marks>=70:
#             return 'C'
#         elif self.marks>=60:
#             return 'D'
#         else:
#             return 'Fail'
#     def __str__(self):
#         return f'Student Name:{self.name}\n,Marks:{self.marks}\nGrade:{self.grade()}'
#     def __add__(self, other):
#         return self.marks+other.marks
#     def __truediv__(self, number):
#         return self.marks/number
#     def __ge__(self, other):
#         return self.marks>=other.marks
#     def __lt__(self, other):
#         return self.marks<other.marks
# s1=Student('Sai Ganesh',92)
# s2=Student('Aditya',82)
# print("Grade s1:",s1.grade())
# print("Grade s2:",s2.grade())
# print("Addition:",s1+s2)
# print("Division:",s1/5)
# print("s1>=s2",s1>=s2)
# print("s1<s2",s1<s2)

'''Question 4: Rectangle Area Comparison
Create a class Rectangle with:
•	attributes: length, breadth 
•	method: area() 
Implement:
•	__str__() 
•	__add__() → add areas of two rectangles 
•	__sub__() → subtract areas 
•	__eq__() → compare areas 
•	__gt__() → check which rectangle has larger area 
•	__getattr__() → handle missing attributes 
•	__setattr__() → length and breadth must be positive '''
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length*self.breadth
#     def __str__(self):
#         return f"length:{self.length}\nbreadth:{self.breadth}\narea:{self.area()}"
#     def __add__(self, other):
#         return self.area()+other.area()
#     def __sub__(self, other):
#         return self.area()-other.area()
#     def __eq__(self, other):
#         return self.area()==other.area
#     def __gt__(self, other):
#         if self.area()>other.area():
#             return f'Rectangle 1 has larger Area'
#         else:
#             return f'Rectangle 2 has larger Area'
# r1=Rectangle(10,5)
# r2=Rectangle(12,6)
# print("Area of r1:",r1.area())
# print("Area of r2:",r2.area())
# print("Addition:",r1+r2)
# print("Subtraction:",r1-r2)
# print("r1=r2:",r1==r2)
# print("r1>r2:",r1>r2)
'''Question 5: Employee Salary System
Create a class Employee with:
•	attributes: name, salary 
•	method: annual_salary() 
Implement:
•	__str__() 
•	__add__() → add salaries of two employees 
•	__mul__() → calculate salary after multiplying by months 
•	__ne__() → check if salaries are not equal 
•	__le__() → check if one salary is less than or equal to another 
•	__getattribute__() → log every attribute access 
•	__setattr__() → salary cannot be below 10000 '''
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def annual_salary(self):
#         return self.salary*12
#     def __str__(self):
#         return f'Name:{self.name}\nSalary:{self.salary}\nAnnual:{self.annual_salary()}'
#     def __add__(self, other):
#         return self.salary+other.salary
#     def __mul__(self, months):
#         return self.salary*months
#     def __ne__(self, other):
#         return self.salary != other.salary
#     def __le__(self, other):
#         return self.salary<=other.salary
# e1=Employee('Sai Ganesh',567890)
# e2=Employee('Divya',77890)
# print("Addition:",e1+e2)
# print("Multiplication:",e1*6)
# print("Not Equal:",e1!=e2)
# print("e1<=e2",e1<=e2)
'''
Question 6: Book Object Comparison
Create a class Book with:
•	attributes: title, author, pages 
•	method: reading_time()
Assume 1 page takes 2 minutes. 
Implement:
•	__str__() 
•	__add__() → add pages of two books 
•	__floordiv__() → divide pages by number of days 
•	__gt__() → compare books based on pages 
•	__eq__() → compare books based on title 
•	__getattr__() → return custom message for missing attribute 
•	__setattr__() → title cannot be empty and pages must be positive '''
# class Book:
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def reading_time(self):
#         return self.pages*2
#     def __str__(self):
#         return f'Book Name:{self.title}\nAuthor:{self.author}\nPages:{self.pages}'
#     def __add__(self, other):
#         return self.pages+other.pages
#     def __floordiv__(self, days):
#         return self.pages//days
#     def __gt__(self, other):
#         return self.pages>other.pages
#     def __eq__(self, other):
#         return self.title==other.title
# b1=Book("Python",'sai',193)
# b2=Book("Java",'ganes',293)
# print("Reading time of b1",b1.reading_time(),"minutes")
# print("Reading time of b2",b2.reading_time(),"minutes")
# print("Addition:",b1+b2)
# print("Floor div:",b1//10)
# print("b1 has more pages:",b1>b2)
# print("Equal:",b1==b2)
'''Question 7: Shopping Cart
Create a class CartItem with:
•	attributes: item_name, price, quantity 
•	method: final_amount() 
Implement:
•	__str__() 
•	__add__() → add final amounts of two cart items 
•	__mod__() → find remainder after applying a discount value 
•	__lt__() → compare item total amount 
•	__ge__() → compare quantity 
•	__getattribute__() → display which attribute is being accessed 
•	__setattr__() → quantity cannot be less than 1 
'''
class CartItem:
    def __init__(self,item_name,price,quantity):
        self.item_name=item_name
        self.price=price
        self.quantity=quantity
    def final_amount(self):
        return self.price*self.quantity
    def __str__(self):
        return f'Item:{self.item_name}\nPrice:{self.price}\nQuantity:{self.quantity}'
    def __add__(self, other):
        return self.final_amount()+other.final_amount()
    def __mod__(self, discount):
        return self.final_amount()%discount
    def __lt__(self, other):
        return self.final_amount()<other.final_amount()
    def __gt__(self, other):
        return self.quantity>=other.quantity
c1=CartItem("Laptop",567890,2)
c2=CartItem("Mouse",890,2)
print('Final Amount:',c1.final_amount())
print('Final Amount:',c2.final_amount())
print("Addition:",c1+c2)
print("Discount:",c1%10)
print("c1<c2:",c1<c2)
print("c1>c2:",c1>c2)
'''Question 8: Time Duration
Create a class TimeDuration with:
•	attributes: hours, minutes 
•	method: total_minutes() 
Implement:
•	__str__() 
•	__add__() → add two time durations 
•	__sub__() → subtract two time durations 
•	__eq__() → compare total minutes 
•	__gt__() → check longer duration 
•	__getattr__() → handle invalid attribute access 
•	__setattr__() → minutes must be between 0 and 59 '''
class TimeDuration:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def total_minutes(self):
        return self.hours*60+self.minutes
    def __str__(self):
        return f'Hours:{self.hours}\nMinutes:{self.minutes}\nTotal:{self.total_minutes()}'
    def __add__(self, other):
        total=self.total_minutes()+other.total_minutes()
        hours=total//60
        minutes=total%60
        return TimeDuration(hours, minutes)
    def __sub__(self, other):
        total = self.total_minutes() + other.total_minutes()
        hours = total // 60
        minutes = total % 60
        return TimeDuration(hours, minutes)
'''Question 9: Laptop Specification
Create a class Laptop with:
•	attributes: brand, ram, price 
•	method: upgrade_ram(extra_ram) 
Implement:
•	__str__() 
•	__add__() → add prices of two laptops 
•	__mul__() → multiply price for bulk purchase 
•	__lt__() → compare price 
•	__eq__() → compare RAM 
•	__getattribute__() → print access message 
•	__setattr__() → RAM and price must be positive '''

'''Question 10: Game Player
Create a class Player with:
•	attributes: name, health, attack_power 
•	method: attack(enemy) 
Implement:
•	__str__() 
•	__add__() → combine attack powers 
•	__sub__() → reduce health after attack 
•	__gt__() → compare health 
•	__eq__() → compare attack power 
•	__getattr__() → return custom message for unavailable player stat 
•	__setattr__() → health cannot go below 0 
'''