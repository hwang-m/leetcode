class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        
        if grid and grid[0]:
            m = len(grid)
            n = len(grid[0])
            step = [(1,0),(0,1),(-1,0),(0,-1)]

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == '1':
                        ans += 1
                        grid[i][j] = '0'
                        stack = [(i, j)]
                        while stack:
                            i0, j0 = stack.pop()
                            for si, sj in step:
                                if 0<=i0+si<m and 0<=j0+sj<n and grid[i0+si][j0+sj]=='1':
                                    stack.append((i0+si, j0+sj))
                                    grid[i0+si][j0+sj] = '0'
        
        return ans
