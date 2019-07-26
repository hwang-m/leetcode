class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        ans = [[] for _ in range(numRows)]
        r = 0
        dr = 1
        
        for char in s:
            ans[r].append(char)
            r += dr
            if r == numRows - 1 or r == 0:
                dr *= -1
        
        return ''.join([''.join(row) for row in ans])
