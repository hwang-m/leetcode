class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        n = len(nums)
        i = n - 1
        new_end = n - 1
        
        while i > 0:
            if i + nums[i] >= new_end:
                new_end = i
            i -= 1
        return nums[0] >= new_end
