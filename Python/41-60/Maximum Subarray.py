class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        ithsum = 0
        minsum = 0
        for val in nums:
            ithsum += val
            maxsum = max(maxsum, ithsum - minsum)
            minsum = min(minsum, ithsum)
        return maxsum
