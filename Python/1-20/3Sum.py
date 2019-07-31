class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        i = 0
        
        def find_first_different(index, step = 1):
            while index >= 0 and index < n and index + step >= 0 and index + step < n and nums[index] == nums[index + step]:
                index += step
            return index + step
        
        while i < n - 2:
            l, r = i + 1, n - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp < 0:
                    l = find_first_different(l)
                elif temp > 0:
                    r = find_first_different(r, -1)
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l = find_first_different(l)
                    r = find_first_different(r, -1)
            i = find_first_different(i)
            
        return ans
