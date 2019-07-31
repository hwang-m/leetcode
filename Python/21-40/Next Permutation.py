class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        if i == 0:
            front = 0
        else:
            valley = i - 1
            while i < len(nums) and nums[i] > nums[valley]:
                i += 1
            nums[valley], nums[i - 1] = nums[i - 1], nums[valley]
            front = valley + 1
        
        end = len(nums) - 1
        while front < end:
            nums[front], nums[end] = nums[end], nums[front]
            front += 1
            end -= 1
