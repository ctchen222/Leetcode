"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return 
        queue = deque([root])
        while queue:
            l = len(queue)
            dummy = Node(0)
            for i in range(l):
                node = queue.popleft()
                dummy.next = node
                dummy = dummy.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root