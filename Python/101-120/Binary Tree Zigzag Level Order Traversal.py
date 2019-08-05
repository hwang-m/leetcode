# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        
        if not root:
            return ans
        
        multiplier = 1
        stack = [root]
        
        while stack:
            temp = []
            for i in range(len(stack)):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(temp[::multiplier])
            multiplier *= -1
        
        return ans
