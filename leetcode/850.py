class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        ev = {}
        for i, (a, b, c, d) in enumerate(rectangles):
            if a not in ev: ev[a] = {}
            if c not in ev: ev[c] = {}
            if b not in ev[a]: ev[a][b] = 0
            if d not in ev[a]: ev[a][d] = 0
            if b not in ev[c]: ev[c][b] = 0
            if d not in ev[c]: ev[c][d] = 0
            
            ev[a][b] += 1
            ev[a][d] -= 1
            ev[c][b] -= 1
            ev[c][d] += 1
            
        # print(ev)
        
        cev = {}
        lx = None
        ret = 0
        for x in sorted(ev.keys()):
            if lx is not None:
                ret += (x - lx) * ln
            for y in ev[x]:
                if y not in cev: cev[y] = 0
                cev[y] += ev[x][y]
                
            st = 0
            op = None
            ln = 0
            for y in sorted(cev.keys()):
                st += cev[y]
                if op is None and st > 0:
                    op = y
                elif op is not None and st == 0:
                    ln += y - op
                    op = None
                    
            lx = x
            
        return ret % (10**9+7)
            
            