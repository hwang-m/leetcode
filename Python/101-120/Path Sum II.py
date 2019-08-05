# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        if not (root.left or root.right):
            if root.val == sum: return [[root.val]]
            else: return []
        
        return [[root.val] + l for l in self.pathSum(root.left, sum - root.val)] + [[root.val] + r for r in self.pathSum(root.right, sum - root.val)]
