class Solution:
    
    memo = {}
    
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        
        if not s in self.memo:
            self.memo[s] =  min(self.minCut(s[i:])
                                for i in range(len(s))
                                if s[:i] == s[i-1::-1]) + 1
        return self.memo[s]
