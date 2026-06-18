k = input()
for i in k: 
    s = lambda x: x not in "AEIOUaeiou"
if s(i):
    print(i)