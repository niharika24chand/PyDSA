#bst

class node:
    def __init__(self, data):
        self. data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = node(data)
        else:
            self.check_insert(self.root, data)

    def check_insert(self, curr, data):
        if data < curr.data:
            if curr.left == None:
                curr.left = node(data)
            else:
                self.check_insert(curr.left, data)

        else:
            if curr.right == None:
                curr.right = node(data)
            else:
                self.check_insert(curr.right, data)


    def preorder(self, node):
            if node:
                print(node.data, end=" ")
                self.preorder(node.left)
                self.preorder(node.right)

    def postorder(self, node):
            if node:
                self.postorder(node.left)
                self.postorder(node.right)
                print(node.data, end=" ")

    def inorder(self, node):
            if node:
                self.inorder(node.left)
                print(node.data, end=" ")
                self.inorder(node.right)


bst = BST()
bst.insert(10)
bst.insert(25)
bst.insert(3)
bst.insert(8)
bst.insert(30)
bst.insert(22)

print("Preorder traversal: ")
bst.preorder(bst.root)
print("\nPostorder traversal: ")
bst.postorder(bst.root)
print("\nInorder traversal: ")
bst.inorder(bst.root)
                