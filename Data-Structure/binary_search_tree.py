class TreeNode():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.val:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.val)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.val)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.val)

    def find(self, value):
        if value < self.val:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        if value > self.val:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True


if __name__ == "__main__":
    tree = TreeNode(10)
    tree.insert(10)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(11)
    tree.insert(15)
    tree.insert(5)

    # tree.inorder_traversal()
    # tree.preorder_traversal()
    tree.postorder_traversal()
    # print(tree.find(2))
