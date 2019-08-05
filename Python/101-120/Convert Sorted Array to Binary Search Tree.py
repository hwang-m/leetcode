# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        front = 0
        end = len(nums)
        avg = int((front + end) / 2)
        
        root = TreeNode(nums[avg])
        root.left = self.sortedArrayToBST(nums[front:avg])
        root.right = self.sortedArrayToBST(nums[avg + 1:end])
        
        return root
