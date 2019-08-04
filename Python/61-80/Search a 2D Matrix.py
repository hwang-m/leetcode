class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        
        while l <= r:
            avg = (l+r) // 2
            i, j = avg // n, avg % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = avg - 1
            else:
                l = avg + 1
        
        return False
