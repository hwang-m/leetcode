class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_re = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            nums_re[i] *= nums_re[i - 1] or 1
        return max(nums + nums_re)
