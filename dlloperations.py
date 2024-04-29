'''#dll end insert
class node:
    def __init__(self,data)-> None:
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self)-> None:
        self.head=None
        self.prev=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i=i.next
l=[1,2,3,4,5]
o=dll()
for i in l:
    o.insertatbeg(i)
o.printing()'''
#front insert dll
'''class node:
    def __init__(self,data)-> None:
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self)-> None:
        self.head=None
        self.prev=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self. head.prev=new
            self.head=new
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i=i.next
l=[1,2,3,4,5]
o=dll()
for i in l:
    o.insertatbeg(i)
o.printing()'''
#reversing a dll
class node:
    def __init__(self,data)-> None:
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self)-> None:
        self.head=None
        self.prev=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self. head.prev=new
            self.head=new
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i=i.next
    def rev(self):
        curr=self.head
        while curr:
            if curr.next==None:
                self.head=curr
            curr.next,curr.prev=curr.prev,curr.next
            curr=curr.prev
l=[1,2,3,4,5]
o=dll()
for i in l:
    o.insertatbeg(i)
o.printing()
o.rev()
o.printing()

