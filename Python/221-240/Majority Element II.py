class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        
        for n in nums:
            if n in count:
                count[n] += 1
            elif len(count) < 2:
                count[n] = 1
            else:
                for num in count:
                    count[num] -= 1
                count = {key:val for key, val in count.items() if val != 0}
        
        return [n for n in count if nums.count(n) > len(nums)//3]
