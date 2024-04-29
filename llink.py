'''a=node(1)
a.next=node(2)
a.next.next=node(3)
print(a,a.data,a.next)
print(a.next,a.next.data,a.next.next)
print(a.next.next,a.next.next.data,a.next.next.next)'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(1)
b=node(2)
c=node(3)
a.next=b
b.next=c
print(a,a.data,a.next)
print(b,b.data,b.next)
print(c,c.data,c.next)
