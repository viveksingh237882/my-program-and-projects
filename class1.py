class computer:
    def __init__(self):
        self.name='vivek' 
        self.age=23
    def compare(self,c2):
        if (self.age==c2.age):
            return True
        else:
            return False
c1=computer()
c2=computer()
c1.name='maa'
c1.age=34
if c1.compare(c2):
    print ("they are same")
else:
    print("they are not same")

#print(c1.name)
print(c1.age)
print(c2.name)

#print(c2.age)
