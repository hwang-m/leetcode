class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # smallest missing positive integer could only be from 1 to n + 1
        # replace other numbers with n+1
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1
        
        # if a number appears, use it as index and convert the value at 
        # that position to negative
        for val in nums:
            i = abs(val) - 1
            if i < n:
                nums[i] = -abs(nums[i])
        
        # find the first non-negative value and return its index
        # if all values are negative, return n + 1
        for i, val in enumerate(nums):
            if val >= 0:
                return i + 1
        return n + 1
