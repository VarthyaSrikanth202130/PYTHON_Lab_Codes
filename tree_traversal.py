"""Q. Program to design a class that accommodates all Tree traversal Types"""

# A class that represents an individual node in a Binary Tree
class Node:                   
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

class Tree:

    def init(self,root):
        self.root = root

    def inorder(self, root):
        if root:
            # Traverse left
            self.inorder(root.left)
            # Traverse root
            print(str(root.val) + "->", end='')
            # Traverse right
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            # Traverse left
            self.postorder(root.left)
            # Traverse right
            self.postorder(root.right)
            # Traverse root
            print(str(root.val) + "->", end='')

    def preorder(self, root):
        if root:
            # Traverse root
            print(str(root.val) + "->", end='')
            # Traverse left
            self.preorder(root.left)
            # Traverse right
            self.preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

t1 = Tree()
print("Inorder traversal ")
t1.inorder(root)
print("\nPreorder traversal ")
t1.preorder(root)
print("\nPostorder traversal ")
t1.postorder(root)