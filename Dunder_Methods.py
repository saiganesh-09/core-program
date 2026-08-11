'''class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, o2):
        x=self.x+o2.x
        y=self.y+o2.y
        return Vector(x,y)
    def __sub__(self, o2):
        x=self.x-o2.x
        y=self.x-o2.y
        return Vector(x,y)|
    V1=Vector()
'''
'''class a:
    def __init__(self,a):
        self.a=a
    def __add__(self, other):
        return self.a+other.a
a1=a(10)
a2=a(20)
print(a1+a2)'''

'''class a:
    def __init__(self,a):
        self.a=a
    def __sub__(self, other):
        return self.a-other.a
a1=a(20)
a2=a(10)
print(a1-a2)'''

'''class a:
    def __init__(self,a):
        self.a=a
    def __mul__(self, other):
        return self.a * other.a
a1=a(5)
a2=a(5)
print(a1*a2)'''

'''class a:
    def __init__(self,a):
        self.a=a
    def __mod__(self, other):
        return self.a * other.a
a1=a(5)
a2=a(2)
print(a1%a2)'''

'''class Student:
    def __init__(self,marks):
        self.marks=marks
    def __ge__(self,z):
        return self.marks>=z.marks
    def __gt__(self, z):
        return self.marks>z.marks
s1=Student(85)
s2=Student(90)
print(s1>s2)'''

'''
