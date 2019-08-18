class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxsquare = 0
        
        if matrix and matrix[0]:
            m, n = len(matrix), len(matrix[0])
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == '0':
                        matrix[i][j] = 0
                    elif matrix[i][j] == '1':
                        if i == 0 or j == 0:
                            matrix[i][j] = 1
                        else:
                            matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
                        maxsquare = max(maxsquare, matrix[i][j])
        
        return maxsquare**2
