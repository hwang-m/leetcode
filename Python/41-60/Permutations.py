class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 or len(nums) == 1:
            return [nums]
        
        return [p[:i] + [nums[0]] + p[i:] for p in self.permute(nums[1:]) for i in range(len(nums))]
