# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
        
        # or this: (less code, more time?)
        # return self.isMirror(root, root)
        
    def isMirror(self, p: TreeNode, q: TreeNode) -> bool:
        if not (p or q):
            return True
        if not (p and q):
            return False
        
        return p.val == q.val and self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
