


def count(list):
    even=0
    odd=0
    for i in list:
        if i % 2==0:
            even +=1
        else:
            odd +=1
    return even,odd
list=[1,12,13,23,2,23,32,34]
even, odd=count(list)
print(even)
print(odd)