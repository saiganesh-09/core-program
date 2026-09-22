'''1.  Create a BankAccount class that stores:
     • account number
     • balance (should not be directly modifiable)
 You must: 1. Make the balance attribute inaccessible from outside.
         2. Provide functions to deposit/withdraw that validate the amount.
         3. Prevent withdrawal if balance becomes negative.
         4. Show what happens if someone tries to modify balance directly and why encapsulation prevents it.'''
# class BankAccount:
#     def __init__(self,acc,balance):
#         self.acc=acc
#         self.__balance=balance #Private
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print("Amount Deposited:",amount)
#         else:
#             print('Deposited Amount must be greater than 0')
#     def withdraw(self,amount):
#         if amount<=0:
#             print("Amount must be greater than 0")
#         elif amount>self.__balance:
#             print("Insufficient Balance")
#         else:
#             self.__balance-=amount
#             print("Amount withdrawn:",amount)
#     def balance(self):
#         print("Current Balance:",self.__balance)
# a=BankAccount('ABC123',345678)
# a.balance()
# a.deposit(5000)
# a.balance()
# a.withdraw(2000)
# a.balance()
''' 2. Design a Student class where marks:
     • should always be between 0 and 100
     • should never be set directly Enable updating marks only through
         a controlled method that performs range checks.
 Demonstrate:
     • trying to assign marks manually
     • why encapsulation protects invalid states '''
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         if 0<=marks<=100:
#             self.__marks=marks
#         else:
#             self.__marks=0
#             print('Invalid')
#     def update(self,marks):
#         if 0<=marks<=100:
#             self.__marks=marks
#             print('Marks updated')
#         else:
#             print('Invalid')
#     def show_marks(self):
#         print('Student:',self.name)
#         print("Marks",self.__marks)
# s=Student('Saiganesh',89)
# s.show_marks()
# s.update(99)
# s.show_marks()
''' 3. Create a SecureFile class that:
     • stores content privately
     • provides a method read(password)
     • refuses access if the password is incorrect
     • logs an "Unauthorized attempt" internally (cannot be accessed from outside) '''
# class SecureFile:
#     def __init__(self,content,password):
#         self.__content=content
#         self.__password=password
#         self.__log=[]
#     def read(self,password):
#         if password==self.__password:
#             return self.__content
#         else:
#             self.__log.append('Unauthorized Attempt')
#             return 'Refused Access'
# s1=SecureFile('Hello my name is saiganesh','12345')
# print(s1.read('12345'))
# print(s1.read('123456'))
'''4.Design an Employee class where:
     • salary is hidden
     • outsiders cannot read salary directly
     • use getter method that logs each access attempt
     • provide a method to update salary but only if the new salary is higher
         (prevent accidental downgrade)'''
# class Employee:
#     def __init__(self,salary):
#         self.__salary=salary
#         self.__logs=[]
#     @property
#     def salary(self):
#         self.__logs.append('Salary Acessed')
#         return self.__salary
#     @salary.setter
#     def salary(self,new_salary):
#         if new_salary>self.__salary:
#             self.__salary=new_salary
# e1=Employee(56789)
# print(e1.salary)
# e1.salary=1234567
# print(e1.salary)
'''5. Create a Product class where:
    • price cannot be negative
    • discount cannot exceed 70%
    • internal final price calculation should not be directly exposed
        Provide only one public method get_final_price(). '''
# class Product:
#     def __init__(self,price):
#         if price>=0:
#             self.__price=price
#         else:
#             raise ValueError('Price cannot be Negative')
#     def final_price(self,discount):
#         if discount>70:
#             return 'Discount cannot exceed more than 70%'
#         else:
#             return (self.__price-((discount/100)*self.__price))
# p1=Product(1234)
# print(p1.final_price(67))
'''6. Create a Character class with: 
    • private _health 
    • methods to damage(points) and heal(points) 
    • health cannot drop below 0 or exceed max limit 
    • expose only current health through a read-only getter'''
# class Character:
#     def __init__(self,name):
#         self.name=name
#         self.__health=100
#     @property
#     def health(self):
#         return self.__health
#     def damage(self,points):
#         self.__health-=points
#         if self.__health<0:
#             self.__health=0
#     def heal(self,points):
#         self.__health+=points
#         if self.__health>100:
#             self.__health=100
# c=Character('Saiganesh')
# print("Health:",c.health)
# c.damage(50)
# print("Damage:",c.health)
# c.heal(50)
# print("Heal:",c.health)
'''7. Create: 
    • An Engine class with private state like temperature 
    • A Car class that uses an Engine but should: 
                o Not allow users to manipulate engine temperature 
                o Only expose methods like start_car() or cool_engine() 
    Demonstrate why giving direct engine access is dangerous.'''
class Engine:
    def __init__(self):
        self.__temperature=30
    def start_engine(self):
        print("Engine Started")
        self.__temperature=90
    def cool(self):
        if self.__temperature>30:
            self.__temperature-=10
    def temperature(self):
        return self.__temperature
class Car:
    def __init__(self):
        self.__engine=Engine()
    def start_car(self):
        self.__engine.start_engine()
        print('Car Started')
    def cool_engine(self):
        self.__engine.cool()
    def show_temperature(self):
        print("Engine Temperature:",self.__engine.temperature())
c=Car()
c.start_car()
c.show_temperature()
c.cool_engine()
c.show_temperature()
'''8. Create a ShoppingCart class where: 
    • items are stored privately 
    • users cannot directly modify item list 
    • only add/remove methods are allowed 
    • provide a method to get a safe copy of the cart items (not direct reference to internal list)'''

'''9. Implement a class incorrectly first: 
    • Attendance stored in a list 
    • Exposed directly so any outside code can modify it Then redesign properly: 
    • Make attendance private 
    • Provide controlled methods for marking attendance only Explain the difference. '''

'''10. Create a class using @property and @setter for a private attribute. 
    Then: 1. Show correct usage 
          2. Show how forgetting to use underscore prefix breaks encapsulation 
          3. Show what happens if you implement a setter without validation Focus: 
                            Python-specific encapsulation pitfalls, misuse of properties.'''