'''def fun(x):
    def fun2():
        print(x)
        print(x.__name__)
        x()
    return fun2

# k = fun(fun3)
# k()
# print(k.__name__)
@fun
def fun3():
    print("World Hello")
# fun3 = fun(fun3)
fun3()

def dec(func):
    def inner(n):
        print("Starting this Function")
        print(func.__name__)
        func(n)
        print("Ending this Function")
    return inner
@dec # greet = dec(greet)
def greet(name):
    print(f"Hello {name}")

print(greet.__name__)
greet("Saiganesh")'''

'''def vaild(func):
    uns = []
    special_char = ['@',"!","#","$","%","^","&","*"]
    def inner(us,psd:str):
        if 8 <= len(psd) <= 15:
            k = list(filter(lambda x: x in special_char, psd))
            n = list(filter(lambda x: x.isdigit(), psd))
            up = list(filter(lambda x: x.isupper(), psd))
            print(k)
            print(n)
            print(up)

            if up and n and k:
                return func(us,psd)
            else:
                return "Invalid Password"
        else:
            return "Minimum length of the password is 8 characters"
    return inner
@vaild
def register(username,password):
    return f"{username}'s Register Successful"

print(register("Saiganesh","Dhaya143$$"))'''

'''def Upper(x):
    for i in x:
        if i.isupper():
            return True
    return False

def valid(func):
    uns = []
    special_char = ['@',"!","#","$","%","^","&","*"]
    def inner(us:str,psd:str,age:int):
        if us not in uns:
            if 8 <= len(psd) <= 15:
                k = list(filter(lambda x: x in special_char, psd))
                n = list(filter(lambda x: x.isdigit(), psd))
                up = Upper(psd)
                # print(k)
                # print(n)
                # print(up)

                if up and n and k:
                    if age >= 18:
                        uns.append(us)
                        return func(us,psd,age)
                    else:
                        return "Age must be greater than 17"
                else:
                    return "Invalid Password"
            else:
                return "Minimum length of the password is 8 characters"
        else:
            return "Username already exists"
    return inner
@valid
def register(username,password,age):
    return f"{username}'s Register Successful"

print(register("sai Te2356789","Dhaya143$$6t",19))'''
#print(register("sai ganesh","Dhaya143$$",19))

'''def addition(func):
    def inner(a,b):
        print(f"The addition of {a} and {b} is equal to ",end=" ")
        print(func(a,b))
    return inner
@addition
def add(a,b):
    return a+b
add(10,5)'''

import functools

def ann(func):
    @functools.wraps(func)
    def inner(x,y):
        # print(func.__name__)
        # print(func.__annotations__)
        # print(func.__doc__)
        print(x,y)
        return func(x,y)
    return inner


@ann
def fun(a:int,b:int) -> int:
    """Just adding a Doc for the function"""
    return a+b

print(fun(10,24))
print(fun.__name__)
print(fun.__annotations__)
print(fun.__doc__)