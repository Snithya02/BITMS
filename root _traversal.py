class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def dfs_inorder(root):
    if root==None:
        return
    dfs_inorder(root.left)
    print(root.data,end=" ")
    dfs_inorder(root.right)
def dfs_postorder(root):
    if root==None:
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.data,end="  ")
def dfs_preorder(root):
    if root==None:
        return
    print(root.data,end=" ")
    dfs_preorder(root.left)
    dfs_preorder(root.right)
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
'''dfs_inorder(root)'''
'''dfs_preorder(root)'''
dfs_postorder(root)