def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

vl=topten()
for i in vl:
    print(i)