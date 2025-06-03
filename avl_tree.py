class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.ht = 1

class AVL_tree:

    def insert(self, node, val):
        if node == None:
            return Node(val)
        else:
            if val < node.data:
                node.left = self.insert(node.left, val)
            else:
                node.right = self.insert(node.right, val)

        node.ht = 1 + max(self.height(node.left), self.height(node.right))
        bal = self.balance(node)

        #left left case
        if bal > 1 and val < node.left.data:
            return self.right_rotate(node)

        #right right case
        if bal < -1 and val > node.right.data:
            return self. left_rotate(node)

        #left right case
        if bal > 1 and val > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        #right left case
        if bal < -1 and val < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    #inorder traversal
    def traversal(self, node):
        if node is not None:
            self.traversal(node.left)
            print(node.data, end=" ")
            self.traversal(node.right)


    def height(self, node):
        return node.ht if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def left_rotate(self, x):
        y = x.right
        t1 = y.left
        y.left = x
        x.right = t1

        x.ht = 1 + max(self.height(x.left), self.height(x.right))
        y.ht = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, x):
        y = x.left
        t2 = y.right
        y.right = x
        x.left = t2

        x.ht = 1 + max(self.height(x.left), self.height(x.right))
        y.ht = 1 + max(self.height(y.left), self.height(y.right))

        return y


tree = AVL_tree()
root = None

values = [10, 20, 30, 40, 50, 25]
for val in values:
    root = tree.insert(root, val)


print("Inorder traversal: ")
tree.traversal(root)