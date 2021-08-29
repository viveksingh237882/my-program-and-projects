#n=int(Input("Enter the valve"))
def fact(n):
    #if n==0:
     #   return 1
    #else f=1:
     #   return 1
    f=1
    for i in  range (1,n+1):
        f=f*i
    return f
x=int(input("Enter the vzlue "))
result=fact(x)
print(result)
