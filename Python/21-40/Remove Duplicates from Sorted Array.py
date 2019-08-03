class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow = fast = 0
        while fast < len(nums) - 1:
            while fast < len(nums) - 1 and nums[fast] == nums[slow]:
                fast += 1
            if nums[fast] != nums[slow]:
                nums[slow + 1] = nums[fast]
                slow += 1
        
        return slow + 1
