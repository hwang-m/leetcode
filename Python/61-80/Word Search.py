class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not (board and board[0]):
            return False
        
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == word[0]:
                    if self.search(board, r, c, word):
                        return True
        return False
    
    
    def search(self, board: List[List[str]], r: int, c: int, word: str) -> bool:
        '''Search for word starting from index (r, c).'''
        if not word:
            return True
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[0]:
            return False
        
        temp = board[r][c]
        board[r][c] = ''
        found = any(self.search(board, r+dr, c+dc, word[1:]) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        board[r][c] = temp
        
        return found
