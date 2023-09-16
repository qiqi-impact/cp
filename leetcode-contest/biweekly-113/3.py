class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        ct = {}
        ret = 0
        for x, y in coordinates:
            for t in range(k+1):
                u = k-t
                ret += ct.get((t^x, u^y), 0)
            ct[(x, y)] = ct.get((x, y), 0) + 1
        return ret