'''from reprlib import recursive_repr
class Playlist:
    def __init__(self,l):
        self.lst=l
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.lst):
            song=self.lst[self.index]
            self.index+=1
            return song
        # else:
        #     raise StopIteration

p1=Playlist(['irumudi','Fear','dude'])
p2=Playlist(['irumudi','Fear','dude'])
p=iter(p2)
for i in p2:
    if i is None:
        break
    print(i)'''

'''class Attendance:
    def __init__(self,st):
        self.students=st
        self.roll_no=0
    def __iter__(self):
        return self.
    def __next__(self):
        if self.roll_no<len(self.students):
            name=self.students[self.roll_no]
            self.roll_no+=1
            return name
        else:
            raise StopIteration
st1=Attendance(["siva","aditya","sai","sathwik"])
st2=Attendance(["Lobu","vamsi","siva","Divya"])
for i in (st1):
    print(f"{i} present")
for j in (st2):
    print(f"{j} present")'''

# class Even:
'''    def __init__(self,l):
        self.l=l
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self,l):
            n=self.l(self.index)
            self.index+=1
            if n%2==0:
                return
a= Even([1,2,3,4,5,6,7])'''

#create a custom iterator that takes the whole sentence and return non-vowels only?
'''class Iterator:
    def __init__(self,n):
        self.n=n
        self.index=0
        self.k=['a','e','i','o','u','A','E','I','O','U']
    def __iter__(self):
        return self
    def __next__(self):
        while self.i<len(self.n):
            self.i+=1
            if self.n[self.i-1] not in "AEIOU":
                return self.s[self.i-1]
        raise StopIteration
c1=Iterator("saiganesh")'''

#Create a custom iterator that takes  a string and returns ASCII values of the character.
'''class ASCIIIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        char = self.text[self.index]
        self.index += 1
        return ord(char)
text = input("Enter a string: ")
obj = ASCIIIterator(text)
for value in obj:
    print(value)'''

#Write a custom iterator that prints numbers from 1 to N.
'''class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
n = int(input("Enter N: "))
obj = NumberIterator(n)
for num in obj:
    print(num)'''

#Create an iterator that returns only even numbers from a given list.
'''class EvenIterator:
    def __init__(self,numbers):
        self.numbers=numbers
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.numbers):
            num=self.numbers[self.index]
            self.index+=1
            if num%2==0:
                return num
        raise StopIteration
numbers=[1,2,3,4,5,6,7,8,9]
obj=EvenIterator(numbers)
for num in obj:
    print(num)'''
#Implement an iterator that iterates over a string character by character in reverse order.
class ReverseString:
    def __init__(self, string):
        self.string = string
        self.index = len(string) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        char = self.string[self.index]
        self.index -= 1
        return char
s = ReverseString("Python")
for char in s:
    print(char)