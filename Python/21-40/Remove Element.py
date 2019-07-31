class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        front, end = 0, len(nums) - 1
        while end > front:
            while nums[front] != val and front < end:
                front += 1
            while nums[end] == val and front < end:
                end -= 1
            
            if nums[end] == val:
                return front
            
            if front != end:
                nums[front], nums[end] = nums[end], nums[front]
                front += 1
                end -= 1
        
        if nums[front] == val:
            return front
        
        return front + 1
