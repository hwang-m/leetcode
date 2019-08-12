class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        
        seen = set()
        ans = set()
        
        for i in range(10, len(s)+1):
            if s[i-10:i] in seen:
                ans.add(s[i-10:i])
            else:
                seen.add(s[i-10:i])
        
        return list(ans)
