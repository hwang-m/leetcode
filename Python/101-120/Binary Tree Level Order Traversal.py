# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        
        if not root:
            return ans
        
        stack = [root]
        children = []
        
        while stack:
            ans.append([])
            while stack:
                node = stack.pop(0)
                ans[-1].append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            stack, children = children, []
        
        return ans
