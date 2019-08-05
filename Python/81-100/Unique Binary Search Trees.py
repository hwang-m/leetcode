class Solution:
    
    memo = {}
    
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        
        if n not in Solution.memo:
            Solution.memo[n] = sum(self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n+1))
        
        return Solution.memo[n]
