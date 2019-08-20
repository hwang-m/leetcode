# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # assume 1 <= k <= number of nodes
        for val in self.inorder(root):
            if k == 1:
                return val
            k -= 1
    
    def inorder(self, root: TreeNode):
        if root:
            yield from self.inorder(root.left)
            yield root.val
            yield from self.inorder(root.right)
