class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in nums:
            if abs(i) < n:
                if nums[abs(i)] != 0:
                    nums[abs(i)] = -abs(nums[abs(i)])
                else:
                    nums[abs(i)] = - (n + 1)
                    nums[0] = -abs(nums[0])
        for i, num in enumerate(nums):
            if num >= 0:
                return i
        return n
