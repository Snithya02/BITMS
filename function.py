class a:
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("fun2")
class b(a):
    def __init__(self)->None:
        print("1")
    def __init__(self)->None:
        print("2")
    def fun(self):
        print("fun3")
    def fun(self):
        print("fun4")
p=b()
p.fun()
p.fun1()

 

