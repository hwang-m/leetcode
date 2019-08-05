# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if (not root) or (not (root.left or root.right)):
            return True
        
        def inorder(root):
            if root:
                yield from inorder(root.left)
                yield root.val
                yield from inorder(root.right)
        
        val = inorder(root)
        a = next(val)
        b = next(val)
        
        while b > a:
            try:
                a, b = b, next(val)
            except StopIteration:
                return True
        
        return False
