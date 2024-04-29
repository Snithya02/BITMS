class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def bfs(root):
        q=[root]
        while q:
           a=q.pop(0)
           print(a.data)
           if a.left:
               q.append(a.left)
           if a.right:
               q.append(a.right)
root=node(4)
root.left=node(2)
root.right=node(6)
root.left.left=node(1)
root.left.right=node(3)
root.right.left=node(5)
bfs(root)