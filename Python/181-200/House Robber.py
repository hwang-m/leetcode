class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        a, b = nums[0], nums[1]
        for val in nums[2:]:
            a, b = max(a, b), max(a + val, b)
        return max(a, b)
