class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        for i in range(m-1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m-1 and j < n-1:
                    grid[i][j] = grid[i][j] + min(grid[i][j+1], grid[i+1][j])
                elif i < m-1:
                    grid[i][j] = grid[i][j] + grid[i+1][j]
                elif j < n-1:
                    grid[i][j] = grid[i][j] + grid[i][j+1]
        
        return grid[0][0]
