class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        ct = {}
        ret = 0
        for x, y in coordinates:
            for t in range(k+1):
                u = k-t
                if t^x not in ct:
                    continue
                if u^y not in ct[t^x]:
                    continue
                ret += ct[t^x][u^y]
            if x not in ct:
                ct[x] = {}
            if y not in ct[x]:
                ct[x][y] = 0
            ct[x][y] += 1
        return ret