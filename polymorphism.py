'''Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
override it.
Demonstrate polymorphism by iterating over a list of different animal objects and calling
make_sound().'''
# class Animal:
#     def make_sound(self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def make_sound(self):
#         print("Dog: Barks")
# class Cat(Animal):
#     def make_sound(self):
#         print("Cat: Meow")
# class Cow(Animal):
#     def make_sound(self):
#         print("Cow: Moo")
# animals=[Dog(),Cat(),Cow()]
# for animal in animals:
#     animal.make_sound()
'''Q2. Write a function operate(device) that calls device.start().
Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
method, but share no inheritance relationship.
Show that Python’s polymorphism works through behavior, not type.'''
# class Car:
#     def start(self):
#         print("Car starts with a key")
# class Computer:
#     def start(self):
#         print("Computer starts with a Button")
# class WashingMachine:
#     def start(self):
#         print("WashingMachine starts with a switch")
# def operate(device):
#     device.start()
# car=Car()
# computer=Computer()
# washing_machine=WashingMachine()
# operate(car)
# operate(computer)
# operate(washing_machine)
'''Q3. Create a Vector class that supports:
• + operator → add coordinates
• == operator → compare equality
Show how operator overloading gives natural polymorphism to user-defined classes.'''
# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self, other):
#         return Vector(self.x+other.x,self.y+other.y)
#     def __eq__(self, other):
#         return self.x==other.x and self.y==other.y
#     def __str__(self):
#         return (f'X:{self.x} Y:{self.y}')
# v1=Vector(1,2)
# v2=Vector(3,4)
# v3=Vector(5,6)
# v4=Vector(7,8)
# print(v1+v2)
# print(v1+v2+v3)
# print(v1==v2)
# print(v3==v4)
'''Q4. Create a base class Transport with move() and derived classes Bus and Bike that
override it but also call the parent implementation using super().
Show the combination of reuse + custom behavior.'''
# class Transport:
#     def move(self):
#         print("Transport")
# class Bus(Transport):
#     def move(self):
#         super().move()
#         print("Bus")
# class Bike(Transport):
#     def move(self):
#         super().move()
#         print("Bike")
# bus=Bus()
# bike=Bike()
# bus.move()
# bike.move()
'''Q5. Using the abc module, create an abstract class Notification with send().
Implement subclasses EmailNotification, SMSNotification, PushNotification — each
with its own send() logic.
Demonstrate polymorphism by looping over all and calling send().'''



'''Q6. Design:
• Base class Payment with process(amount)
• Subclass CreditCardPayment adds process(amount, card_type)
Demonstrate what happens when overriding with different signatures and how Python
handles it.'''
# class Payment:
#     def process(self,amount):
#         print("amount")
# class CreditCardPayment(Payment):
#     def process(self,amount,card_type):
#         print("Crdit_Payment")
#         super().process(amount)
# p=Payment()
# p.process(2345)
# c=CreditCardPayment()
# c.process(1234,"silver")
'''Q7. Create:
• Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS,
each implementing a different logic method.
Demonstrate how polymorphism can be achieved without inheritance by using
interchangeable strategy objects.'''

'''Q8. Create:
• Base Account → withdraw()
• Subclass SavingsAccount → modifies withdraw()
• Subclass PremiumSavingsAccount → overrides again but calls parent using super()
Show how polymorphism works across multiple levels.'''
'''Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and
Rectangle, each implementing a draw() method.
Add another unrelated class Car with draw() and pass it — what happens and why?'''
# def draw(shape):
#     shape.draw()
# class Circle:
#     def draw(self):
#         print("Circle")
# class Square:
#     def draw(self):
#         print("Square")
# class Rectangle:
#     def draw(self):
#         print("Rectangle")
# class Car:
#     def draw(self):
#         print("Car")
# l=[Circle(),Square(),Rectangle(),Car()]
# for i in l:
#     draw(i)
'''Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a
pay() method.
Now implement a version that checks types explicitly using isinstance() before calling
pay().
Compare both designs and explain why one breaks the spirit of polymorphism.'''