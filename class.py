class computer:
    def __init__(self,cpu,ram) :
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("vivek singh",self.cpu,self.ram)
comp1=computer(22,35)
com2=computer('raisen','ios')
computer.config()
computer.config()
print(comp1)
print(com2)