# class User:
#     def __init__(self,n,a,g,dob):
#         self.name=n
#         self.age=a
#         self.gender=g
#         self.dob=dob
#     def login(self):
#         print('Successfully Logged in')
#     def logout(self):
#         print('successfully logged out')
# print(User.mro())
# class Instagram(User):
#     def post(self):
#         print(f'{self.name} post got 1M likes')
# a1=Instagram('saiganesh',15,'Male','23-07-2004')
# a1.post()
# a1.login()
# a1.logout()
# print(Instagram.mro())
# print('-'*50)

# class Restaurants:
#     def __next__(self,n,r,add):
#         self.name=n
#         self.rating=r
#         self.address=add
#     def display_menu(self):
#         print('All Dishes are non-veg only')
# class Swiggy(User,Restaurants):
#     def display(self):
#         print(f'Name:{self.name}\n'
#               f'Age:{self.age}\n'
#               f'Gender:{self.gender}\n'
#               f'Dob:{self.dob}')
#     def display(self):
#         print('user"s details')
# print(Swiggy.mro())
# class Zomato(User,Restaurants):
#     def display(self):
#         print('Zomato')
# print(Zomato.mro())
# class Customer(Swiggy,Zomato):
#     def order(self):
#         print('Just Ordered')
# c1=Swiggy('saiganesh',35,'Male','23-07-2004')
# c1.display()
# print(Customer.mro())
# print('-'*50)

# class Bank(User):
#     Name='RBI'
#     def guide_lines(self):
#         print('Beware of Scammer and Call 0004')
# class Bhim_UPI(Bank,Swiggy):
#     def Payments(self,amount):
#         print(f'{self.amount} has been paid through UPI')
# b1=Bhim_UPI('Shiva',21,'male','11-09-2004')
# b1.display()
# print(Bhim_UPI.mro())
# print('-'*50)

'''• Create a base class Animal with a method sound().
Create a derived class Dog
that overrides the sound() method.
Demonstrate method overriding'''
from random import choice
from unittest import addModuleCleanup

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks")
# a=Animal()
# d=Dog()
# a.sound()
# d.sound()

'''• Create class A with method show(). 
Create class B(A) that overrides show() 
and also calls the parent method using super().'''
# class A:
#     def show(self):
#         print("This method shows class A")
# class B(A):
#     def show(self):
#         print("This method shows class B")
#         super().show()
# obj=B()
# obj.show()

'''Create multi-level inheritance with classes A → B → C, 
each having a method display() printing the class name. 
Create object of C and call display(), showing method resolution.'''
# class A:
#     def display(self):
#         print("Class A")
# class B(A):
#     def display(self):
#         print("Class B")
# class C(B):
#     def display(self):
#         print("Class C")
# obj=C()
# obj.display()

'''• Implement hierarchical inheritance using a base class Vehicle and two child
classes Car and Bike, each defining a method wheels().'''
#        Vehicle
#         /   \
#       Car  Bike
# class Vehicle:
#     def vehicle_type(self):
#         print("This is a Vehicle")
# class Car(Vehicle):
#     def wheels(self):
#         print("Car has 4 wheels")
# class Bike(Vehicle):
#     def wheels(self):
#         print("Bike has 2 wheels")
# #Create Objects
# c=Car()
# b=Bike()
# #Call Methods
# c.vehicle_type()
# c.wheels()
#
# b.vehicle_type()
# b.wheels()

'''• Create class Employee with an instance method salary().
Create class Manager(Employee) that overrides salary() and adds an incentive. 
Demonstrate both outputs.'''
# class Employee:
#     def salary(self):
#         print("Employee salary:30,000")
# class Manager(Employee):
#     def salary(self):
#         print("Manager salary:50,000")
#         print("Manager incentive:10,000")
# e=Employee()
# m=Manager()
# e.salary()
# m.salary()

'''Create class University with a class variable and a class method. 
Inherit it into class College and access the parent’s class variable from the child class'''
# class university:
#     university="Parul University"
#     @classmethod
#     def data_analytics(cls):
#         print("passed out")
# class college(university):
#     pass
# a=college()
# print(a.university)
# print(university.university)
# print(college.university)

''' Create class MathOps with a static method add(a, b). 
# Create class AdvancedOps(MathOps) and use the static method without overriding it.'''
# class MathOps:
#     @staticmethod
#     def add(a,b):
#         return a+b
# class AdvancedOps(MathOps):
#     pass
# o=AdvancedOps()
# r=o.add(5,8)
# print(r)

'''Create two classes Father and Mother, both defining a method skills(). 
Create class Child(Father, Mother) and check which skills() runs using MRO.'''
# class Father:
#     def skills(self):
#         print("Father's skill: Driving")
#         super().skills()
# class Mother:
#     def skills(self):
#         print("Mother's skill: Cooking")
# class Child(Father,Mother):
#     def skills(self):
#         print('child skills')
#         super().skills()
# c=Child()
# c.skills()
# print("\nMRO:")#Method Resolution Order
# print(Child.mro())

'''• Create an abstract class Shape with an abstract method area(). Create class
Rectangle(Shape) that implements the area() method.'''

'''• Create class Person with a constructor __init__(name). Create class
Student(Person) with constructor __init__(name, roll). Use super() to call the
parent constructor'''
# class Person:
#     def __init__(self,name):
#         self.name=name
# class Student(Person):
#     def __init__(self,name,roll):
#         super().__init__(name)
#         self.roll=roll
#     def display(self):
#         print("Name:",self.name)
#         print("Roll No:",self.roll)
# s=Student("Saiganesh",22)
# s.display()

'''1. Bank Management System
Create a Bank class with:
• balance variable
• deposit()
• withdraw()
• check_balance()
Create a User class that inherits Bank and displays the user's name. Perform
deposit, withdrawal, and balance check.'''
# class Bank:
#     def __init__(self,balance=0):
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print("Amount deposited:",amount)
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print("Amount withdrawn:",amount)
#         else:
#             print("Insufficient balance")
#     def check_balance(self):
#         print("Current Balance:",self.balance)
# class User(Bank):
#     def __init__(self,name,balance=0):
#         super().__init__(balance)
#         self.name=name
#     def display_user(self):
#         print("User Name:",self.name)
# u=User("Saiganesh",5000)
# u.display_user()
# u.deposit(2000)
# u.withdraw(1500)
# u.check_balance()

'''2. Employee Salary System
Create an Employee class with:
• emp_name
• salary
• display_details()
Create a Manager class that inherits Employee and adds a bonus(). Display the
total salary'''
# class Employee:
#     def __init__(self,emp_name,salary):
#         self.emp_name=emp_name
#         self.salary=salary
#     def display_details(self):
#         print("Employee Name:",self.emp_name)
#         print("Salary:",self.salary)
# class Manager(Employee):
#     def __init__(self,emp_name,salary,bonus):
#         super().__init__(emp_name,salary)
#         self.bonus=bonus
#     def display_total_salary(self):
#         self.display_details()
#         print("Bonus:",self.bonus)
#         print("Total Salary:",self.salary+self.bonus)
#
# a=Manager("Sai Ganesh",50000,10000)
# a.display_total_salary()
'''3. Student Result System
Create a Student class with:
• Name
• marks
• display_marks()
Create a Result class that inherits Student and calculates whether the student has
passed or failed.'''
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display_marks(self):
#         print("Student_Name:",self.name)
#         print("Marks:",self.marks)
#
# class Result(Student):
#     def check_result(self):
#         self.display_marks()
#         if self.marks>=40:
#             print("Passed")
#         else:
#             print("Failed")
# s=Result("Sai Ganesh",85)
# s.check_result()

'''4. Food Ordering System Using Multilevel Inheritance
Class 1: Restaurant
• Create a method menu(item) that returns the price of the selected food
item.
Class 2: FoodCourt (inherits Restaurant)
Create the following methods:
• display_menu() – Display the available food items.
• order() – Accept the food item from the user and allow multiple orders.
• billing() – Display the total bill and add a packing charge of ₹20.
Class 3: Customer (inherits FoodCourt)
• Create an object of the Customer class.
• Call the order() method. '''
# class Restaurant:
#     def menu(self,item):
#         prices= {
#             "pizza": 150,
#             "burger": 100,
#             "biryani": 200,
#             "dosa": 80,
#             "idly": 50
#         }
#         return prices.get(item,"item not there")
# class FoodCourt(Restaurant):
#     def display_menu(self):
#         print("\n----- MENU -----")
#         print("Pizza   - ₹150")
#         print("Burger  - ₹100")
#         print("Biryani - ₹200")
#         print("Dosa    - ₹80")
#         print("Idly    - ₹50")
#     def order(self):
#         self.display_menu()
#         total=0
#         while True:
#             item=input("\nEnter food item:")
#             if item=="done":
#                 break
#             price=self.menu(item)
#             if price==0:
#                 print("Item not available")
#             else:
#                 total+=price
#                 print(item, "added - ₹", price)
#         self.billing(total)
'''5. Movie Ticket Booking System Using Multilevel Inheritance
Class 1: Movie
• Create a method ticket(movie) that returns the ticket price.
Class 2: Booking (inherits Movie)
Create the following methods:
• movies() – Display the available movies.
• selection() – Allow the user to book multiple tickets.
• billing() – Display the total amount and add a booking charge of ₹30.
Class 3: Customer (inherits Booking)
• Create an object and call the selection() method. '''
# class Movie:
#     def ticket(self,movie):
#         prices = {
#             "pushpa": 150,
#             "bahubali": 180,
#             "rrr": 200,
#             "kgf": 170,
#             "salaar": 160
#         }
#         return prices.get(movie.lower(), 0)
# class Booking(Movie):
#     def movies(self):
#         print("\n----- AVAILABLE MOVIES -----")
#         print("Pushpa  - ₹150")
#         print("Bahubali - ₹180")
#         print("RRR     - ₹200")
#         print("KGF     - ₹170")
#         print("Salaar  - ₹160")
#     def selection(self):
#         self.movies()
#         total=0
#         while True:
#             movie=input("\nEnter movie name: ")
#             if movie=="done":
#                 break
#             price=self.ticket(movie)
#             if price==0:
#                 print("Movie not available")
#             else:
#                 total+=price
#                 print(movie,"Ticket Booked -",price)
#         self.billing(total)
#     def billing(self,total):
#         booking_charge=30
#         final_amount=total+booking_charge
#         print("\n----- BILL -----")
#         print("Ticket Total   : ₹", total)
#         print("Booking Charge : ₹", booking_charge)
#         print("Total Amount   : ₹", final_amount)
# class Customer(Booking):
#     pass
# c=Customer()
# c.selection()

'''6. Online Course Enrollment System Using Multilevel Inheritance
Class 1: Course
• Create a method fee(course) that returns the course fee.
Class 2: Academy (inherits Course)
Create the following methods:
• courses() – Display available courses.
• enroll() – Allow the user to enroll in multiple courses.
• billing() – Display the total fee and add a registration fee of ₹100.
Class 3: Student (inherits Academy)
• Create an object and call the enroll() method'''
# class Course:
#     def fee(self,course):
#         fees={
#             "python": 5000,
#             "java": 6000,
#             "sql": 4000,
#             "web development": 7000,
#             "data science": 8000
#         }
#         return fees.get(course.lower(), 0)
# class Academy(Course):
#     def courses(self):
#         def courses(self):
#             print("\n----- AVAILABLE COURSES -----")
#             print("Python          - ₹5000")
#             print("Java            - ₹6000")
#             print("SQL             - ₹4000")
#             print("Web Development - ₹7000")
#             print("Data Science    - ₹8000")
#     def enroll(self):
#         self.courses()
#         total=0
#         while True:
#             course=input("\nEnter Course Name:",)
#             if course=="done":
#                 break
#             amount=self.fee(course)
#             if amount==0:
#                 print("Course not available")
#             else:
#                 total+=amount
#                 print(course, "enrolled successfully - ₹", amount)
#         self.billing(total)
#     def billing(self,total):
#         registration_fee=100
#         final_amount=total+registration_fee
#         print("\n----- BILL -----")
#         print("Course Fee       : ₹", total)
#         print("Registration Fee : ₹", registration_fee)
#         print("Total Amount     : ₹", final_amount)
# class Student(Academy):
#     pass
# s=Student()
# s.enroll()

'''7. Cab Booking System Using Hierarchical Inheritance
Class 1: Cab
• Create methods to calculate the fare for Bike, Auto, and Car rides.
Class 2: Uber (inherits Cab)
• Create the methods menu(), booking(), and billing().
• Add 10% GST and apply a 15% discount if the bill is above ₹1000.
Class 3: Ola (inherits Cab)
• Create the methods menu(), booking(), and billing().
• Add 12% GST and apply a 20% discount if the bill is above ₹1500.
Driver Code
• Ask the user to choose Uber or Ola and call the booking() method
              Cab
             /   \
            /     \
         Uber     Ola'''
# class Cab:
#     def Bike_Fare(self,km):
#         return km*10
#     def Auto_Fare(self,km):
#         return km*10
#     def Car_Fare(self,km):
#         return km*10
# class Uber(Cab):
#     def menu(self):
#         print("\n----- UBER -----")
#         print("1. Bike - ₹10/km")
#         print("2. Auto - ₹15/km")
#         print("3. Car  - ₹20/km")
#     def booking(self):
#         self.menu()
#         choice=input("Choose ride: ")
#         km=float(input("Enter distance in km: "))
#
#         if choice=="bike":
#             fare=self.Bike_Fare(km)
#         elif choice=="auto":
#             fare=self.Auto_Fare(km)
#         elif choice=="car":
#             fare=self.Car_Fare(km)
#         else:
#             print("Invalid Choice")
#             return
#         self.billing(fare)
#     def billing(self,fare):
#         gst=fare*0.10
#         discount=0
#         if fare>1000:
#             discount=fare*0.15
#         total=fare+gst-discount
#         print("\n----- UBER BILL -----")
#         print("Base Fare : ₹", fare)
#         print("GST (10%) : ₹", gst)
#         print("Discount  : ₹", discount)
#         print("Total Bill: ₹", total)
# class Ola(Cab):
#     def menu(self):
#         print("\n----- UBER -----")
#         print("1. Bike - ₹10/km")
#         print("2. Auto - ₹15/km")
#         print("3. Car  - ₹20/km")
#     def booking(self):
#         self.menu()
#         choice=input("Choose ride: ")
#         km=float(input("Enter distance in km: "))
#
#         if choice=="bike":
#             fare=self.Bike_Fare(km)
#         elif choice=="auto":
#             fare=self.Auto_Fare(km)
#         elif choice=="car":
#             fare=self.Car_Fare(km)
#         else:
#             print("Invalid Choice")
#             return
#         self.billing(fare)
#     def billing(self,fare):
#         gst=fare*0.12
#         discount=0
#         if fare>1500:
#             discount=fare*0.20
#         total=fare+gst-discount
#         print("\n----- OLA BILL -----")
#         print("Base Fare : ₹", fare)
#         print("GST (10%) : ₹", gst)
#         print("Discount  : ₹", discount)
#         print("Total Bill: ₹", total)
#
# print("----- CAB BOOKING -----")
# print("1. Uber")
# print("2. Ola")
#
# choice = input("Choose Cab: ")
# if choice=="uber":
#     u=Uber()
#     u.booking()
# elif choice=="ola":
#     o=Ola()
#     o.booking()
# else:
#     print("Invalid cab")

'''8. Grocery Shopping System Using Hierarchical Inheritance
Class 1: Grocery
• Create methods to return the price of Rice, Sugar, and Oil.
Class 2: Dmart (inherits Grocery)
• Create the methods items(), shopping(), and billing().
• Add 5% GST and apply a 10% discount if the bill is above ₹2000.
Class 3: Reliance Smart (inherits Grocery)
• Create the methods items(), shopping(), and billing().
• Add 5% GST and apply a 15% discount if the bill is above ₹2500.
Driver Code
• Ask the user to choose the supermarket and call the shopping() method.'''
# class Grocery:
#     def rice_price(self,quantity):
#         return quantity*60
#     def sugar_price(self,quantity):
#         return quantity*45
#     def oil_price(self,quantity):
#         return quantity*50
# class Dmart(Grocery):
#     def items(self):
#         print("\n----- DMART ITEMS -----")
#         print("Rice  - ₹60/kg")
#         print("Sugar - ₹45/kg")
#         print("Oil   - ₹120/litre")
#     def shopping(self):
#         self.items()
#         total=0
#         while True:
#             item=input("\nEnter item: ")
#             if item=="done":
#                 break
#             quantity=float(input("Enter Quantity: "))
#             if item=="rice":
#                 price=self.rice_price(quantity)
#             elif item=="sugar":
#                 price=self.sugar_price(quantity)
#             elif item=="oil":
#                 price=self.oil_price(quantity)
#             else:
#                 print("Item not available")
#                 continue
#             total+=price
#             print(item, "added - ₹", price)
#         self.billing(total)
#     def billing(self,total):
#         gst=total*0.5
#         discount=0
#         if total>2000:
#             discount=total*0.10
#         final_amount=total+gst-discount
#
#         print("\n----- DMART BILL -----")
#         print("Total Amount : ₹", total)
#         print("GST (5%)     : ₹", gst)
#         print("Discount     : ₹", discount)
#         print("Final Bill   : ₹", final_amount)
# class RelianceSmart(Grocery):
#     def items(self):
#         print("\n----- RELIANCE MART ITEMS -----")
#         print("Rice  - ₹60/kg")
#         print("Sugar - ₹45/kg")
#         print("Oil   - ₹120/litre")
#     def shopping(self):
#         self.items()
#         total=0
#         while True:
#             item=input("\nEnter item: ")
#             if item=="done":
#                 break
#             quantity=float(input("Enter Quantity: "))
#             if item=="rice":
#                 price=self.rice_price(quantity)
#             elif item=="sugar":
#                 price=self.sugar_price(quantity)
#             elif item=="oil":
#                 price=self.oil_price(quantity)
#             else:
#                 print("Item not available")
#                 continue
#             total+=price
#             print(item, "added - ₹", price)
#         self.billing(total)
#     def billing(self,total):
#         gst=total*0.5
#         discount=0
#         if total>2500:
#             discount=total*0.15
#         final_amount=total+gst-discount
#
#         print("\n----- RELIANCE MART BILL -----")
#         print("Total Amount : ₹", total)
#         print("GST (5%)     : ₹", gst)
#         print("Discount     : ₹", discount)
#         print("Final Bill   : ₹", final_amount)
#
# print("----- GROCERY SHOPPING -----")
# print("1. Dmart")
# print("2. Reliance Smart")
# choice=input("Choose SuperMart: ")
# if choice=="Dmart":
#     d=Dmart()
#     d.shopping()
# elif choice=="Reliance Smart":
#     r=RelianceSmart()
#     r.shopping()

'''9. Bus Ticket Booking System Using Hierarchical Inheritance
Class 1: Bus
• Create methods to return the fare for Sleeper, Semi-Sleeper, and AC
buses.
Class 2: RedBus (inherits Bus)
• Create the methods routes(), booking(), and billing().
• Add 10% GST and a reservation charge of ₹30.
Class 3: AbhiBus (inherits Bus)
• Create the methods routes(), booking(), and billing().
• Add 10% GST and a reservation charge of ₹20.
Driver Code
• Ask the user to choose the platform and call the booking() method.'''
# class Bus:
#     def sleeper_fare(self,distance):
#         return distance*3
#     def semi_sleeper_fare(self,distance):
#         return distance*2.5
#     def ac_fare(self,distance):
#         return distance*4
# class Redbus(Bus):
#     def routes(self):
#         print("\n----- REDBUS ROUTES -----")
#         print("1. Hyderabad to Vijayawada")
#         print("2. Hyderabad to Visakhapatnam")
#         print("3. Hyderabad to Bangalore")
#     def booking(self):
#         self.routes()
#         bus_type=input("\n Enter bus type:")
#         distance=float(input("Enter distance in km:"))
#         if bus_type=="sleeper":
#             fare=self.sleeper_fare(distance)
#         elif bus_type=="semi_sleeper":
#             fare=self.semi_sleeper_fare(distance)
#         elif bus_type=="ac":
#             fare=self.ac_fare(distance)
#         else:
#             print("Invalid Bus Type")
#             return
#         self.billing(fare)
#     def billing(self,fare):
#         gst=fare*0.10
#         reservation_charge=30
#         total=fare+gst+reservation_charge
#         print("\n----- REDBUS BILL -----")
#         print("Bus Fare           : ₹", fare)
#         print("GST (10%)          : ₹", gst)
#         print("Reservation Charge : ₹", reservation_charge)
#         print("Total Amount       : ₹", total)
# class AbhiBus(Bus):
#     def routes(self):
#         print("\n----- ABHI BUS ROUTES -----")
#         print("1. Hyderabad to Vijayawada")
#         print("2. Hyderabad to Visakhapatnam")
#         print("3. Hyderabad to Bangalore")
#     def booking(self):
#         self.routes()
#         bus_type=input("\n Enter bus type:")
#         distance=float(input("Enter distance in km:"))
#         if bus_type=="sleeper":
#             fare=self.sleeper_fare(distance)
#         elif bus_type=="semi_sleeper":
#             fare=self.semi_sleeper_fare(distance)
#         elif bus_type=="ac":
#             fare=self.ac_fare(distance)
#         else:
#             print("Invalid Bus Type")
#             return
#         self.billing(fare)
#     def billing(self,fare):
#         gst=fare*0.10
#         reservation_charge=20
#         total=fare+gst+reservation_charge
#         print("\n----- ABHI BUS BILL -----")
#         print("Bus Fare           : ₹", fare)
#         print("GST (10%)          : ₹", gst)
#         print("Reservation Charge : ₹", reservation_charge)
#         print("Total Amount       : ₹", total)
# print("----- BUS TICKET BOOKING -----")
# print("1. RedBus")
# print("2. AbhiBus")
# choice=input("choose platform: ")
# if choice==Redbus:
#     r=Redbus()
#     r.booking()
# elif choice==AbhiBus:
#     a=AbhiBus()
#     a.booking()
'''10. ATM System Using Multiple Inheritance
Class 1: SBI
• Create the methods deposit(amount) and check_balance().
Class 2: UnionBank
• Create the methods withdraw(amount) and mini_statement().
Class 3: ATM (inherits SBI and UnionBank)
• Create the methods menu() and transaction().
• Allow the user to perform banking operations.
Driver Code
• Create an object of the ATM class.
• Call the transaction() method'''
class SBI:
    def __init__(self):
        self.balance=5000
    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited:",amount)
    def check_balance(self):
        print("Current Balance:",self.balance)

class UnionBank:
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Amount withdrawn:",amount)
            