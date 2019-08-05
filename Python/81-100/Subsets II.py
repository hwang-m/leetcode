class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        n = nums.count(nums[0])
        ans = []
        
        for subset in self.subsetsWithDup(nums[1:]):
            if subset.count(nums[0]) == n - 1:
                ans.extend([subset, [nums[0]] + subset])
            else:
                ans.append(subset)
        
        return ans
