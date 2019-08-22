class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i in range(len(nums)):
            if nums[i]:
                if not nums[zeros]:
                    nums[i], nums[zeros] = nums[zeros], nums[i]
                zeros += 1
