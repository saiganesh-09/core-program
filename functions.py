'''def power(base,exponent):
    return base ** exponent
print(power(8,3))
'''

'''sum=0
for i in range(1,101):
    if i%2==0:
        sum=sum+i
print(sum)'''

'''def fun(base,exponent):
    return base ** exponent
result=fun(2,3)
print(result)'''


'''
def ful_name(*a):
    print(*a)
ful_name("panila","hemasundara","rao")'''


'''def fun(name,city,hobby):
     print(name,city,hobby)
fun("panila","hyderabad","coding")'''


'''def fun(a,b):
    return a-b
print(fun(10,3))
print(fun(3,10))'''


'''def send_mail(to,subject,body):
    print(f"To{to}, Subject: {subject}, Body: {body}")
send_mail("john@example.com", "Hello", "How are you?")'''


'''def profile(username,email,age):
    print(f"username: {username}, email: {email}, age: {age}")
profile(username="panila", email="john@gmail.com", age= 23)'''


'''
def fun(name ,city):
    print(name,city)
fun(name="hyderabad","panila")
#first argument should be keyword argument and then positional argument.
othrtwise it will give an error.
'''


'''def person(name,*hobbies):
    print(name,hobbies)
person("Alice","Reading","Traveling","Cooking")'''


'''def f(*args):
    print(type(args))
f(1,2,3)'''
##*args collects multiple arguments into a tuple.



'''def fun(a,b,*arg,**kws):
    print(a,b,arg,kws)
fun(1,2,3,4,5,name="Alice",age=21)'''