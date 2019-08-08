class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while nums[l] > nums[r]:
            avg = (l+r)//2
            if nums[avg] >= nums[l]:
                l = avg + 1
            else:
                r = avg
        
        return nums[l]
