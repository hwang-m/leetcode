class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        i, j = 0, 0
        di, dj = 0, 1
        
        for num in range(n**2):
            ans[i][j] = num + 1
            if i+di < 0 or i+di >= n or j+dj < 0 or j+dj >= n or ans[i+di][j+dj] != 0:
                di, dj = dj, -di
            i, j = i + di, j + dj
        
        return ans
