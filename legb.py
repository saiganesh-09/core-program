#global
'''
x=10
def fun():
    global x
    x=x+10
    print(x)
fun()'''

#Non local:
#global
def fun():
    #enclosure
    def fun2():
         #local
         x=10
         x=x+35
         print(x)
    fun2()
fun()