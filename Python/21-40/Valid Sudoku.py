class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:[] for i in range(9)}
        cols = {j:[] for j in range(9)}
        cells = {c:[] for c in range(9)}
        
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == '.':
                    continue
                elif val in rows[i] or val in cols[j] or val in cells[3*(i//3)+j//3]:
                    return False
                rows[i].append(val)
                cols[j].append(val)
                cells[3*(i//3)+j//3].append(val)
        
        return True
