def fun(x:int,y:int) -> int:
    print(x+y)
    return x*y
fun(2,5)
print(fun.__name__)
print(fun.__annotations__)