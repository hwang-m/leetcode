# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        
        stack = [(root, 0)]
        maxlevel = -1
       
       while stack:
            node, level = stack.pop()
            if level > maxlevel:
                ans.append(node.val)
                maxlevel = level
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        
        return ans
