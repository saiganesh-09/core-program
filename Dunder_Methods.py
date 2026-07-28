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

class Student:
    def __init__(self,marks):
        self.marks=marks
    def __ge__(self,z):
        return self.marks>=z.marks
    def __gt__(self, z):
        return self.marks>z.marks
s1=Student(85)
s2=Student(90)
print(s1>s2)