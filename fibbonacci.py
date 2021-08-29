n=int(input("Enter the lenght of number"))
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        if c<=12:
            print(c)
        else:
            print("u don't want to print")
        
fib(n)
