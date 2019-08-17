class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = end = 0
        partial_sum = 0
        minlen = float('inf')
        
        # two pointers both go through the nums list once
        for start in range(len(nums)):
            while end < len(nums) and partial_sum < s:
                partial_sum += nums[end]
                end += 1
            # break out of the loop if the end pointer is already at the end and the partial sum is less than s
            # since partial sum decreases as start pointer moves forward
            if end >= len(nums) and partial_sum < s:
                break
            
            minlen = min(minlen, end - start)
            partial_sum -= nums[start]
        
        if minlen == float('inf'):
            return 0
        return minlen
