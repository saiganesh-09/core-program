'''def intro (name,city,hobby):
    print(f"{name} lives in {city} enjoys {hobby}")
intro("sai","vizag","eating")'''

'''def subtract(a,b):
    return a-b
print(subtract(10,3))
print(subtract(3,10))'''

'''def bio(first_name,last_name,age):
    print(f"{first_name} {last_name} {age}")
bio("sai","ganesh",21)
'''

def two_params(a, b):
    return a + b

try:
    two_params(1, 2, 3)
except TypeError as e:
    print("Error:", e)