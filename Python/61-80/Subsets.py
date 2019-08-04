class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        ans = []
        for subset in self.subsets(nums[1:]):
            ans.extend([subset, [nums[0]] + subset])
        return ans
