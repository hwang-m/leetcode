class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board and board[0]:
            m, n = len(board), len(board[0])
            step = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            border = [(i, j) for i in range(m) for j in range(n) if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O']
            
            # go through the border and change any connected 'O' to 'B'
            while border:
                i, j = border.pop()
                board[i][j] = 'B'
                border.extend([(i+si,j+sj) for (si, sj) in step if 0<= i+si < m and 0 <= j + sj < n and board[i+si][j+sj] == 'O'])
            
            # go through the board and change any remaining 'O' to 'X'
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    elif board[i][j] == 'B':
                        board[i][j] = 'O'
