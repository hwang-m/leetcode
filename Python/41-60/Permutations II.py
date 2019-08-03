class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 or len(nums) == 1:
            return [nums]
        
        ans = []
        for p in self.permuteUnique(nums[1:]):
            for i in range(len(p) + 1):
                ans.append(p[:i] + [nums[0]] + p[i:])
                if i < len(p) and p[i] == nums[0]:
                    break
        return ans
