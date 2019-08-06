class Solution:
    def partition(self, s: str) -> List[List[str]]:        
        if not s:
            return [[]]
        
        return [[s[:i]] + part 
                for i in range(1, len(s)+1) 
                if self.isPal(s[:i]) 
                for part in self.partition(s[i:])]
    
    
    def isPal(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        return False
