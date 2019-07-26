class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        setnums = set(nums)
        ans_w_repeat = []
        ans_wo_repeat = []
        
        for i, val in enumerate(nums):
            if target - val in setnums:
                ans_w_repeat.append(i)
                if target - val != val:
                    ans_wo_repeat.append(i)
        
        if ans_wo_repeat == []:
            return ans_w_repeat
        
        return ans_wo_repeat
