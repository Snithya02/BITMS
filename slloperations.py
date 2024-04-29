'''class node:
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
l=[1,2,3,4,5]
o=sll()
for i in l:
    o.insertatbeg(i)
o.printing()'''
                       #end insert
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self)->None:
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            i=self.head
            while i.next:
                i=i.next
            i.next=new
    def printing(self):
        if self.head==None:
            return
        i=self.head
        while i:
            print(i.data)
            i=i.next
    def length(self):
        count=0
        i=self.head
        while i:
            i=i.next
            count+=1
        return count
l=[1,2,3,4,5,9]
o=sll()
for i in l:
    o.insertatend(i)
o.printing()#printing the elements of the list
print(o.length())#returns the length of the list in number'''
#reversing of singly linked list
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
    def rev(self):
        prev=None
        curr=self.head
        nxt=self.head.next
        while curr:
            curr.next=prev
            prev=curr
            curr=nxt
            if nxt:
                nxt=nxt.next
        self.head=prev
    def printing(self):
        if self.head==None:
            return
        i=self.head
        while i:
            print(i.data)
            i=i.next
l=[1,2,3,4,5]
o=sll()
for i in l:
    o.insertatbeg(i)
o.printing()
o.rev()
o.printing()      
       

