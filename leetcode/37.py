class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def parse(idx):
            a, b = idx//9, idx%9
            return a//3, b//3, a, b

        cell_taken = [[set() for _ in range(3)] for _ in range(3)]
        row_taken = [set() for _ in range(9)]
        col_taken = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    v = int(board[i][j])
                    cell_taken[i//3][j//3].add(v)
                    row_taken[i].add(v)
                    col_taken[j].add(v)

        def dfs(idx):
            if idx == 81:
                return True
            sr, sc, cx, cy = parse(idx)
            
            if board[cx][cy] != '.':
                return dfs(idx+1)
            
            for i in range(1, 10):
                if i not in cell_taken[sr][sc] and i not in row_taken[cx] and i not in col_taken[cy]:
                    cell_taken[sr][sc].add(i)
                    row_taken[cx].add(i)
                    col_taken[cy].add(i)
                    board[cx][cy] = str(i)
                    if dfs(idx+1):
                        return True
                    board[cx][cy] = '.'
                    cell_taken[sr][sc].discard(i)
                    row_taken[cx].discard(i)
                    col_taken[cy].discard(i)
        dfs(0)




