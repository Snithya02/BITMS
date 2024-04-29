def fun(a,b):
    print(a,b)
fun(2,3)
def fun(a,b=0):
    print(a,b)
fun(2,5)
def fun(a,b=0):
    print(a,b)
fun(b=2,a=5)
def fun(a,*b):
    print(a,b)
fun(4,5,6,7,8)
a=[1,2,3,4]
b=a
b[0]=5
print(a)
def fun(a):
    print(a)
b=560
fun(b)