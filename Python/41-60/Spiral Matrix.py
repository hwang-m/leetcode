class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        seen = set()
        ans = []
        
        i, j = 0, 0
        di, dj = 0, 1
        
        for _ in range(m * n):
            ans.append(matrix[i][j])
            seen.add((i,j))
            if not (i+di, j+dj) in seen and i+di>=0 and i+di<m and j+dj>=0 and j+dj<n:
                i, j = i + di, j + dj
            else:
                di, dj = dj, -di
                i, j = i + di, j + dj
        
        return ans
