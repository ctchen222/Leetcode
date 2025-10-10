

# import queue
from collections import deque


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


# 廣度優先搜尋：queue


def bfs_tra(root):
    result = []
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)
    return result


print(bfs_tra(r))
