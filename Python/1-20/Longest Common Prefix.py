class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        
        i = -1
        for i, l in enumerate(zip(*strs)):
            if l != (l[0],) * len(strs):
                return strs[0][:i]
            
        return strs[0][:i+1]
