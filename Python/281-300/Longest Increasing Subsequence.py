class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        n = len(nums)
        count = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    count[i] = max(count[i], count[j] + 1)
        
        return max(count)
