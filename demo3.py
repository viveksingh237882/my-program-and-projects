from array import *
arr = array('i',[])
n=int(input("Enter the size of array"))
for i in range(n):
    x=int(input("Enter the value "))
    arr.append(x)
print(arr)
k=0
v=int(input("Enter the value for search"))
for e in  arr:
    if e==v:
        print(k)
        break
k+=1