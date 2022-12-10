class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        D = list(pairwise([-1, 0, 1, 0, -1]))
        def hits_edge(i, j):
            board[i][j] = 1
            ret = i == 0 or i == R-1 or j == 0 or j == C-1
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for dx, dy in D:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == 'O':
                        if nx == 0 or nx == R-1 or ny == 0 or ny == C-1:
                            ret = True
                        board[nx][ny] = 1
                        q.append((nx, ny))
            return ret
        
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
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    v = 2 if hits_edge(i, j) else 3
                    switch(i, j, 1, v)
                    
        for i in range(R):
            for j in range(C):
                if board[i][j] == 2:
                    switch(i, j, 2, 'O')
                if board[i][j] == 3:
                    switch(i, j, 3, 'X')
        return board