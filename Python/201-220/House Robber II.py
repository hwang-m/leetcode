class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        return max(self.robI(nums[:-1]), self.robI(nums[1:]))
        
    def robI(self, nums: List[int]) -> int:
        a, b = nums[0], nums[1]
        for val in nums[2:]:
            a, b = max(a, b), max(a+val, b)
        return max(a, b)
