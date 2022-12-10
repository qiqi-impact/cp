class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        D = list(pairwise([-1, 0, 1, 0, -1]))
        
        def switch(i, j, t, c):
            board[i][j] = c
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for dx, dy in D:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == t:
                        board[nx][ny] = c
                        q.append((nx, ny))
        
        for i in [0, R-1]:
            for j in range(C):
                if board[i][j] == 'O':
                    switch(i, j, 'O', '-')
                    
        for j in [0, C-1]:
            for i in range(R):
                if board[i][j] == 'O':
                    switch(i, j, 'O', '-')
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'

        return board