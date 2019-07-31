class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        
        if nums[-1] < target:
            return len(nums)
        
        index = 0
        while nums[index] < target:
            index += 1
        return index
