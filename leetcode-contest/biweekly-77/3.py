class Solution:
    def countUnguarded(self, r: int, c: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        g = [[0 for _ in range(c)] for _ in range(r)]
        ct = 0
        for x, y in guards:
            g[x][y] = 1
            ct += 1
        for x, y in walls:
            g[x][y] = 2
            ct += 1
            
        seen = set()
            
        for x in range(r):
            grd = False
            ss = set()
            for y in range(c):
                if g[x][y] == 0:
                    ss.add((x,y))
                elif g[x][y] == 1:
                    grd = True
                    seen |= ss
                    ss = set()
                elif g[x][y] == 2:
                    if grd:
                        seen |= ss
                    grd = False
                    ss = set()
            if grd:
                seen |= ss
                    
        for y in range(c):
            grd = False
            ss = set()
            for x in range(r):
                if g[x][y] == 0:
                    ss.add((x,y))
                elif g[x][y] == 1:
                    grd = True
                    seen |= ss
                    ss = set()
                elif g[x][y] == 2:
                    if grd:
                        seen |= ss
                    grd = False
                    ss = set()
            if grd:
                seen |= ss
            
        return r*c - len(seen) - ct