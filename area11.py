import math
class circle:
    def __init__(self,radius):
        self.r=radius
    def printing(self):
        print(math.pi*self.r*self.r)
class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def printing(self):
        print(self.l*self.b)
l=float(input())
b=float(input())
r=float(input())
o=circle(r)
o1=rectangle(l,b)
o.printing()
o1.printing()       