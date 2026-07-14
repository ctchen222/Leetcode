# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def flatten(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: None Do not return anything, modify root in-place instead.
    #     """
    #     # extra space version
    #     # time: O(n)
    #     # space: O(n)
    #     nodes = []
    #     def preorder(node):
    #         if not node: return
    #         nodes.append(node)
    #         preorder(node.left)
    #         preorder(node.right)
        
    #     preorder(root)
    #     for i in range(len(nodes) - 1):
    #         nodes[i].left = None
    #         nodes[i].right = nodes[i + 1]
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        current = root
        while current:
            if current.left:
                cursor = current.left
                while cursor.right:
                    cursor = cursor.right
                cursor.right = current.right
                current.right = current.left
                current.left = None
            current = current.right
                    
