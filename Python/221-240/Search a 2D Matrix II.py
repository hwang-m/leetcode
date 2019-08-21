class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix and matrix[0]:
            i = len(matrix[0]) - 1
            for row in matrix:
                while row[i] > target and i > 0:
                    i -= 1
                if row[i] == target:
                    return True
        
        return False
