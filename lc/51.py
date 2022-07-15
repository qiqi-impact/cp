class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        selections = []
        coltaken = set()
        plustaken = set()
        minustaken = set()
    
        def dfs(row):
            if row == n:
                board = []
                for x in selections:
                    board.append('.'*(x) + 'Q' + '.'*(n-1-x))
                ret.append(board)
            else:
                for col in range(n):
                    if row+col in plustaken:
                        continue
                    if row-col in minustaken:
                        continue
                    if col in coltaken:
                        continue
                    selections.append(col)
                    coltaken.add(col)
                    plustaken.add(row+col)
                    minustaken.add(row-col)
                    dfs(row+1)
                    coltaken.discard(col)
                    plustaken.discard(row+col)
                    minustaken.discard(row-col)
                    selections.pop()
        dfs(0)
        return ret