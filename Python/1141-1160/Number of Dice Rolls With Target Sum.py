class Solution:
    
    memo = {}
    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > d*f: return 0
        if d == 1 or target == d or target == d*f: return 1
        
        if (d, f, target) in self.memo:
            return self.memo[(d,f,target)]
        
        ans = 0
        for i in range(1, f+1):
            ans += self.numRollsToTarget(d-1, f, target - i)
        self.memo[(d,f,target)] = ans % (10**9+7)
        
        return self.memo[(d,f,target)]
