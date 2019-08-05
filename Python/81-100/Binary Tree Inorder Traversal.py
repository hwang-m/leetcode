# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        #____________recursive_solution____________#
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
        #____________iterative_solution____________#
        stack = [root]
        ans = []
        while stack:
            while root.left:
                stack.append(root.left)
                root = stack[-1]
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
                root = stack[-1]
        return ans
