class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def expand(start, end):
            while start > 0 and end < n - 1 and s[start - 1] == s[end + 1]:
                start -= 1
                end += 1
            return s[start : end + 1]
        
        ans = ''
        for i in range(n):
            odd_pali = expand(i, i)
            if len(odd_pali) > len(ans):
                ans = odd_pali
            if i + 1 < n and s[i] == s[i + 1]:
                even_pali = expand(i, i + 1)
                if len(even_pali) > len(ans):
                    ans = even_pali
                    
        return ans
