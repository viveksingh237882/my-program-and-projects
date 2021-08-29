
from functools import reduce
nums=[14,12,15,15,158,14,16,15,12,5,5]
evens=list(filter(lambda n: n%2==0,nums))
double=list(map(lambda n: n*2,evens))
sum=reduce(lambda a,b: a+b),double))
pritn(sum)
print(evens)
print(double)