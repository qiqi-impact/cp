class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        x, y = 0, 0 # current pos
        D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dp = 0 # which direction we are in. notice D[1] is D[0] turned by 90 degrees, D[2] is D[1] turned by 90 degrees, etc. so we just increment by 1 to turn
        ret = []
        for i in range(R*C):
            # grab x,y cell and stick in ret
            ret.append(matrix[x][y])
            matrix[x][y] = None
            
            # try next cell in same direction
            nx, ny = x+D[dp][0], y+D[dp][1]
            if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] is not None:
                x, y = nx, ny
            else:
                # oh no, we ran into a None or edge, turn!
                dp = (dp+1)%4
                nx, ny = x+D[dp][0], y+D[dp][1]
                x, y = nx, ny
        return ret