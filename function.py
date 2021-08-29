def count(lista):
    even=0
    odd=0


    for i in range (lista(0,n)):
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even ,odd

lista=[]
n=int(input("Enter the size of list"))
for i in range (0,n):
    i+=1
    print("Enter the element ")
    element=int(input())
    lista.append(element)
print("The enteried list",lista)
even, odd=count(lista)
print(even)
print(odd)

