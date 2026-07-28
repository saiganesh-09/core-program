'''class Student:
    total_students=0
    pass_marks=35
    total_marks=100
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.total_students+=1
    @staticmethod
    def is_passed():
        if self.marks>=Student.pass_marks:
            print("passed")
        else:
            print("Failed")
    @instancemethod
    def curve_marks(self):
        m=(self.marks*100)/100
        return m
    @staticmethod
    def utility(marks):
        if self.marks>90:
            print("A")
        elif self.marks>80:
            print("B")
        else:
            print("C")
s1=Student("sai",95)
s1.is_passed()
s1.curve_marks()
s1.utility()
print(Student.total_students)

'''

'''class Employee:
    company_name="Tech"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        Employee.company_name=new_name
E1=Employee("Sai")
print(E1)
print(E1.name)
E2=Employee("Sai")
print(E1.company_name)
print(E2.company_name)
Employee.change_company("cvcorp")
print(E1.company_name)
print(E2.company_name)'''

'''class MathOps:
    @staticmethod
    def is_even(num):
        return num%2==0
print("Using class:")
print(MathOps.is_even(10))
print(MathOps.is_even(7))
obj = MathOps()
print("\nUsing Instance:")
print(obj.is_even(24))
print(obj.is_even(15))'''

