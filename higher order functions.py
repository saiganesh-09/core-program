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


'''l=[0,1,2,3,4,5,6,7,8,9]
A=list(map(lambda x:x+1,l))
B=list(filter(lambda y:y%2==1,A))
C=sorted(B,key=lambda z:z>5)
from functools import reduce
D=reduce((lambda p,q:p+q,C))'''

'''l=[0,1,2,3,4,5,6,7,8,9]
D=reduce(lambda p,q:p+q,sorted(filter(lambda y:y%==1,map(lambda x:x+1,l)),key=lambda x:z>5))'''

'''2. Given two lists:
a = [1, 2, 3, 4] b = [10, 20, 30, 40]
Use map() with a lambda to create a new list containing the sum of corresponding
elements.
What happens if the lists are of unequal length?'''
# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# r=list(map(lambda x,y:x+y,a,b))
# print(r)

'''3. Given a list:
nums = [12, 15, 7, 18, 20, 21, 25]
Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by
5 but NOT divisible by both.
Explain how the logical condition works.'''
# nums = [12, 15, 7, 18, 20, 21, 25]
# r=list(filter(lambda x:(x%3==0) or (x%5==0),nums))
# print(r)

'''4. Given a list:
nums = [1, 2, 3, 4]
Use reduce() with a lambda to compute the sum, but start with an initial value
of 10.
Explain how the initial value affects the reduction process.'''
# from functools import reduce
# nums = [1, 2, 3, 4]
# r=reduce(lambda x,y:x+y,nums,10)
# print(r)

'''5. Consider the code below:
nums = [[1, 2], [3, 4], [5, 6]] result = list(map(lambda x: x.append(10), nums))
print("Result:", result) print("Nums:", nums)
Questions
• What will be the output of result?
• What will be the output of nums?
• Why does map() behave this way with list.append()?
• How can you modify the lambda so that nums is not changed?'''
# nums = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda x: x.append(10), nums))
# print("Result:", result)
# print("Nums:", nums)

# nums = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda x:x+[10], nums))
# print("Result:", result)
# print("Nums:", nums)

#1.  Use map() with a lambda to add 5 to every element of the following nested list
# l=[[1, 2], [3, 4], [5, 6]]
# r=list(map(lambda x:list(map(lambda y:y+5,x)),l))
# print(r)

'''2. Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
filter() to keep only the keys whose values are greater than 50.'''
# d = {"apple": 100, "banana": 40, "cherry": 150}
# r=list(filter(lambda x:d[x]>50,d))
# print(r)

'''3. Use functools.reduce() with a lambda to find the largest number from a given
list Dynamically'''
# from functools import reduce
# l=list(map(int,input().split()))
# g=reduce(lambda x,y:x if x>y else y,l)
# print("greatest numbers:",g)

'''4. What happens if the lambda passed to reduce() accepts only one parameter or
three parameters? Explain the output or error.'''
# n="saiganesh"
# r=list(map(ord,n))
# print(r)

#6. Use filter() to remove all vowels from a string and print the final string.
'''n="saiganesh"
r=list(filter(lambda x:x.lower() not in 'aeiou',n))
print(r)'''

'''7. Use reduce() to concatenate a list of characters into a single string.
Example input: ['S', 'a', 'i', 'g', 'a', 'n','s','h'].'''
from functools import reduce
# n=['S', 'a', 'i',' ', 'G', 'a', 'n','e','s','h']
# r=reduce(lambda x,y:x+y,n)
# print(r)

'''8. Given a list of integers, use map() with id() to print the memory address
of each element.
Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.'''
# n=[10, 350, 10, 350, 20]
# r=list(map(id,n))
# print(r)

# n=[10, 350, 10, 350, 20]
# print(list(map(id,n)))

'''9. Given a list of numbers:
[5, 10, 15, 20, 25, 30]
Perform the following in a single pipeline:
• Use map() to square each number
• Use filter() to keep only numbers divisible by 5
• Use reduce() to calculate the sum of remaining numbers'''
# from functools import reduce
# n=[5, 10, 15, 20, 25, 30]
# r=reduce(lambda x,y:x+y,filter(lambda x:x%5==0,map(lambda x:x**2,n)))
# print(r)

'''Q1. Use map() to convert a list of temperatures in Celsius to Fahrenheit. Formula: F = (C ×
9/5) + 32'''
# l=[5, 10, 15, 20, 25, 30]
# r=list(map(lambda c:(c*9/5)+32,l))
# print(r)

'''Use filter() to extract all words from a list that start with a capital letter.'''
# w=['Sai','ganesh','Aditya','sathwik']
# r=list(filter(lambda x:x[0].isupper(),w))
# print(r)

'''Q3. Use reduce() to find the product of all numbers in a list: [1, 2, 3, 4, 5] → 120'''
# from functools import reduce
# l=[1, 2, 3, 4, 5]
# r=reduce(lambda x,y:x*y,l)
# print(r)

'''Q4. Sort a list of tuples (name, age) by age in descending order using sorted() with a
lambda key.'''
# s=[('sai',21),('ganesh',24),('aditya',18),('sathwik',22)]
# r=sorted(s,key=lambda x:x[1],reverse=True)
# print(r)

'''Q7. Use reduce() to find the longest string in a list: ['cat', 'elephant', 'dog', 'rhinoceros']'''
# from functools import reduce
# l=['cat', 'elephant', 'dog', 'rhinoceros']
# r=reduce(lambda x,y:x if len(x)>len(y) else y,l)
# print(r)