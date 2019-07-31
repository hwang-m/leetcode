class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = sum(nums[0:3])
        
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                tempsum = nums[i] + nums[l] + nums[r]
                if tempsum == target:
                    return target

                if abs(tempsum - target) < abs(ans - target):
                    ans = tempsum

                if tempsum < target:
                    l += 1
                else:
                    r -= 1
            
        return ans
