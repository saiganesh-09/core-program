#3. Write a program to merge two lists into a single list.
# l1=list(map(int,input().split()))
# l2=list(map(int,input().split()))
# l1.extend(l2)
# print(*l1)
# print(*l2)
#4. Write a program to remove a specific element from a list.
# l=[10,20,30]
# n=int(input())
# if(n in l):
#     l.remove(n)
#     print(*l)
# else:
#     print("Invalid Input")
# #5. Write a program to remove an element from a list using its index.
# l=[10,20,30,40]
# i=int(input())
# n=l.pop(i)
# print(n)
# print(*l)
# n=l.pop()
# print(k)
# print(*l)
l=[1,2,3,4,5,2,3,4,3,4]
n=2
# l.remove(2)
# print(l)
# l.remove(2)
# print(l)
k=l.count(n)
print(k)
for i in range(k):
    l.remove(n)
    print(l)