from sortedcontainers import SortedList

class Solution:
    def totalScore(self, h: int, d: List[int], r: List[int]) -> int:
        n = len(r)
        sl = SortedList()
        ret = 0
        sm = 0
        for i in range(n-1, -1, -1):
            sl.add(h - r[i] + sm)
            sm += d[i]
            ret += len(sl) - sl.bisect_left(sm)
        return ret