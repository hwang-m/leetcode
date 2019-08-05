# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    memo = {}
    
    def generateTrees(self, n: int, m = 1) -> List[TreeNode]:
        """generate unique BST's that store values from m to n."""
        if m > n:
            return []
        if m == n:
            return [TreeNode(n)]
        
        if (n, m) in Solution.memo:
            return Solution.memo[(n, m)]
        
        ans = []
        
        for i in range(m, n+1):
            for left_root in self.generateTrees(i-1, m) or [None]:
                for right_root in self.generateTrees(n, i+1) or [None]:
                    root = TreeNode(i)
                    root.left = left_root
                    root.right = right_root
                    ans.append(root)
        
        Solution.memo[(n, m)] = ans
        return ans
