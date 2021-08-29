


from typing import ValuesView


class student:
    school='vivek singh'
    def __init__(self, m1,m2,m3) :
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self):
        self.m1=ValuesView
    @classmethod
    def info(cls):
        return cls.school
    

s1= student(26,45454,45654)
s2=student(232,232,233)
print(s1.m1,s2.m2)
print(student.info)
print(s1.avg())