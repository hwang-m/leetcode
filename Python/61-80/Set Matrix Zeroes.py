class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in rows:
            matrix[i] = [0] * n
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0
