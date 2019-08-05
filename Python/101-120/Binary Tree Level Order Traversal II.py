# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        current = [root]
        children = []
        
        while current:
            ans.append([])
            while current:
                node = current.pop(0)
                ans[-1].append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            current, children = children, []
        
        return ans[::-1]
