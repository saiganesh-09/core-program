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
Demonstrate creating two accounts and using all operations.
-----------------------------------------------------------------------------------------------'''
class BankAccount:
    def __init__(self,account_holder,acc_num,balance=0):
        self.name=account_holder
        self.acc_num=acc_num
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    def withdraw(self,amount):
        self.balance-=amount0
        return self.withdraw
    def __str__(self):
        return f"Account_holder:{self.name}\nAccount_Number:{self.acc_num}\nBalance:{self.balance}"
    def __add__(self, other):
        return self.balance+other.balance
    def __sub__(self, other):
        if self.balance>other.balance:
            return self.balance-other.balance
        else:
            return other.balance-self.balance
    def __eq__(self, other):
        return self.balance==other.balance
    def __lt__(self, other):
        if self.balance<other.balance:
            return f"{c1.name} has less amount"
        else:
            return f"{c2.name} has less amount"
c1=BankAccount("sai",12345,67889)
c2=BankAccount("aditya",67890,123454)
# print(c1)
# print(c2)
print(c1.deposit(5000))
print(c2.deposit(6000))
c1.withdraw(500)
c2.withdraw(600)
# print(c1)
# print(c2)
print(c1==c2)
print(c1<c2)

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
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return f"{self.name}buys at {self.price} of {self.quantity}"
    def __add__(self, other):
        return self.price+other.price
    def __sub__(self, other):
        return self.price-other.price
    def __mul__(self, other):
        return self.price*other.price
    def __gt__(self, other):
        return self.price>other.price


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