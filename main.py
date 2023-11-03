class XYZ:
    x1=0
    y1=1
    z1=3
    def __init__(self,x,y,z):
        self.x1=x
        self.y1=y
        self.z1=z
    def printvalues(self):
        print("The Values of x,y,z are",self.x1,self.y1,self.z1)
    def changevalues(self):
        self.x1=10
        self.y1=9
        self.z1=0
class ABC(XYZ):
    a=9
    b=10
    c=9
    def __init__(self, x, y, z,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        super().__init__(x, y, z)
    @classmethod
    def getprintABC(self):
        print('The Value of X,Y,Z',self.a,self.b,self.c)
    @staticmethod
    def add(x,y):
        print(x+y)


myobj=ABC(1,2,3,4,5,6)
myobj.getprintABC()
myobj.printvalues()
myobj.add(1,2)