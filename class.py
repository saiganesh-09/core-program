'''Q1. Create a class Student with instance attributes name and marks.
Add an instance method is_passed() that returns True if marks > 40.
Then create 2 student objects and print whether each has passed or failed.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks>40:
            return True
S1=Student("sai",50)
S2=Student("ganesh",30)
if S1.is_passed():
    print("Passed")
else:
    print("Fail")
if S2.is_passed():
    print("Passed")
else:
    print("Fail")'''

'''Q2. Create a class Employee with attributes name and company_name = "TechCorp".
Add a class method change_company(cls, new_name) to update the company name for all employees.
Demonstrate how this change affects all instances.'''
'''class Employee:
    company_name="TechCorp"
    @classmethod
    def change_company(cls,new_name):
        cls_name=new_name
E1=Employee()
print(E1.company_name)
E1=Employee()
E1.change_company("CV Corp")
print(E1.company_name)'''

'''Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
Then call it both from the class and an instance.
class Mathops:
    @staticmethod
    def is_even(num):
        return num % 2==0
print(Mathops.is_even(3))
S1=Mathops()
print(S1.is_even(4))'''

'''Q4. Create a class Car with:
•	instance attribute mileage
•	class attribute wheels = 4
Add an instance method display_specs() that prints mileage and wheels.
Then change wheels using a class method, and print again.

class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display_specs(self):
        print("mileage",self.mileage)
        print("wheels",self.wheels)
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels
c1=Car(50)
c1.display_specs()
c1.change_wheels(10)'''

'''Q5. Create a class Temperature with:
•	instance attribute celsius
•	a static method to_fahrenheit(celsius)
•	an instance method show_conversion() that uses the static method to print both values.'''

class Temperature:
    def __int__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_farenheit(c):
        return (celsius * 9 / 5) + 32
    def show_conversion(self):
        print("celsius",self.c)
        print(self.to_farenheit(self.celsius))
T1=Temperature(50)
T.show_conversion()