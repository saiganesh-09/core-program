#Reduce":
'''from functools import reduce
l=[1,2,3,4,5]
k= reduce (lambda x,y: x+y,l)
print(k)'''
from functools import reduce

'''from functools import reduce
l=['cat', 'elephant', 'dog', 'rhinoceros']
k= reduce (lambda x,y: x if len(x)>=len(y) else y,l)
print(k)'''

#Filter:
'''a=['Sai','ganesh']
b=list(filter(lambda a: a[0].isupper(),a ))
print(b)'''

#Sorted:
'''people = [('sai', 25), ('ganesh', 35)]
sorted_people = sorted(people, key=lambda x: x[1], reverse=True)
print(sorted_people)
'''

#Map:


'''l=[22,10,30,40]
k=list(map(lambda c:(c *9/5) + 32,l))
print(k)'''

'''l=[0,1,2,3,4,5,6,7,8,9]
A=list(map(lambda x:x+1,l))
B=list(filter(lambda y:y%2==1,A))
C=sorted(B,key=lambda z:z>5)
from functools import reduce
D=reduce((lambda p,q:p+q,C))'''

'''l=[0,1,2,3,4,5,6,7,8,9]
D=reduce(lambda p,q:p+q,sorted(filter(lambda y:y%==1,map(lambda x:x+1,l)),key=lambda x:z>5))'''