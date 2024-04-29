class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self)->None:
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(1)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def printing(self):
        if self.head==None:
            return
        i=self.head
        while i:
            print(i.data)
            i=i.next
    def delatbeg(self):
        '''self.head=self.head.next
        self.head.prev=None'''
        i=self.head
        self.head=self.head.next
        i.next=None
    def delatend(self):
        i=self.head
        while i.next.next:
            i=i.next
        i.next=None
l=[1,2,3,4,5]
o=sll()
for i in l:
    o.insertatbeg(i)
o.printing()
o.delatbeg()
o.printing()
o.delatend()
o.printing()