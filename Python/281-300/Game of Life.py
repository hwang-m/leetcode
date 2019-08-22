class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board and board[0]:
            # Go through the board once, assign 3 to the cells that die, and 2 to the cells that become alive.
            neighbors = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
            m = len(board)
            n = len(board[0])
            
            for i in range(m):
                for j in range(n):
                    live = 0
                    for ni, nj in neighbors:
                        if 0<=i+ni<m and 0<=j+nj<n and board[i+ni][j+nj]%2 == 1:
                            live += 1
                    if board[i][j] == 0 and live == 3:
                        board[i][j] = 2
                    elif board[i][j] == 1 and (live < 2 or live > 3):
                        board[i][j] = 3
                    
            # Then go through the board again to change 3 into 0 and 2 into 1.
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 2: board[i][j] = 1
                    elif board[i][j] == 3: board[i][j] = 0
