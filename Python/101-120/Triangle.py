class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        assert triangle and triangle[0]
        
        for i, row in enumerate(triangle[1:]):
            for j, val in enumerate(row):
                if j == 0:
                    triangle[i+1][j] = triangle[i][j] + val
                elif j == len(row) - 1:
                    triangle[i+1][j] = triangle[i][j-1] + val
                else:
                    triangle[i+1][j] = min(triangle[i][j-1], triangle[i][j]) + val
                
        return min(triangle[-1])
