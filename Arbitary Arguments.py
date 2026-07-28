#Args:
'''def add(*args):
    total=0
    for num in args:
        total+=num
    return total
print(add(1,2,3))'''
from os import name

'''def mul(*args):
    t=1
    for n in args:
        t*=n
    return t
print(mul(10,20,30))'''

'''def f(*args):
    print(type(args))
f(1, 2, 3)
'''

#Kwargs:
'''def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_info(name="Sai",age=21,location="Hyderabad")'''


'''def describe_person(name,*hobbies):
    print(f"Name is  {name} hobbies: {hobbies}")
describe_person("saiganesh","eating","coding")
describe_person("aditya","drinking")
describe_person("siva","eating",)'''

