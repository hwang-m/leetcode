# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.ROB(root))
        
    def ROB(self, root: TreeNode) -> int:
        if not root: return 0, 0
        # return a tuple of length 2
        # first value corresponds to robbing the root
        # second value corresponds to not robbing the root
        left, right = self.ROB(root.left), self.ROB(root.right)
        return root.val + left[1] + right[1], max(left) + max(right)
