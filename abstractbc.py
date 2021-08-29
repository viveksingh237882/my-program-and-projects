from abc import ABCMeta,abstractmethod



class shape(ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0






class Rectangle(shape):

    Type='Rectangle'
    side=4
    type='Rectsngle'
    
    def __init__(self):
        self.width=12
        self.len=12
    def printarea(self):
        return self.len*self.width
a=Rectangle()
print(a.printarea)