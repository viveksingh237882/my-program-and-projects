


class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self,brand,ram,cpu):
            self.brand=brand
            self.ram=ram
            self.cup=cpu
    def show(self):
        print(self.brand,self.ram,self.cpu)
s2=student('vivek singh',12)
s1=student('ranjeet',1)
s1.show()
print(s2.name,s2.rollno) 
lap1=student.laptop('macbook',120,'i10')
lap1.show()