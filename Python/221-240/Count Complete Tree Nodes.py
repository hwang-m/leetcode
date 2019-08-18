# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        h = self.height(root)
        return self.countNodes1(root, h)
    
    def countNodes1(self, root: TreeNode, h: int) -> int:
        if h == 0: return 0
        
        if self.height(root.right) == h-1:
            return 2**(h-1) + self.countNodes1(root.right, h-1)
        else:
            return self.countNodes1(root.left, h-1) + 2**(h-2)
        
    def height(self, root: TreeNode) -> int:
        h = 0
        node = root
        while node:
            h += 1
            node = node.left
        return h
