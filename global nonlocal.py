'''x=200
def fun():
    x=300
    def fun2():
        nonlocal x
        def fun3():
            nonlocal x
            print(x)
        fun3()
    fun2()
fun()'''
nb