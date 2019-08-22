# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        if not (root.left or root.right): return [str(root.val)]
        
        return [str(root.val) + '->' + path for child in (root.left, root.right) for path in self.binaryTreePaths(child)]
