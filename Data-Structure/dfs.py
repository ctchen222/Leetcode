class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


c1l = TreeNode(3)
c1r = TreeNode(4)
c2l = TreeNode(4)
c2r = TreeNode(3)
c1 = TreeNode(val=2, left=c1l, right=c1r)
c2 = TreeNode(val=2, left=c2l, right=c2r)
r = TreeNode(val=1, left=c1, right=c2)


# 往右dfs
def dfs_right(root):
    result = []
    stack = []
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        result.append(node.val)
        if node.left != None:  # 先放左子節點
            stack.append(node.left)
        if node.right != None:
            stack.append(node.right)
    return result

# 往左dfs


def dfs_left(root):
    result = []
    stack = []
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        result.append(node.val)
        if node.right != None:  # 先加入右子節點
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
    return result


print(dfs_right(r))
print(dfs_left(r))
