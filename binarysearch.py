

pos=-1

def search(lst,n):
    l=0
    u=len(lst)-1
    while l<=u:

        mid=(l+u)//2
        if lst[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if mid < n:
                l=mid+1
            else:
                u=mid-1
    return False 


lst=[2,3,4,5,6,7,8,9]
n=5

if search(lst,n):
    print("found",pos+1)
else:
     print("not found")
