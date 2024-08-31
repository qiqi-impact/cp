class Solution:
    def minDamage(self, p: int, d: List[int], h: List[int]) -> int:
        class cmp(int):
            def __lt__(self, other):
                return h[self] * d[other] < h[other] * d[self]
        n = len(d)
        h = [(x + p - 1) // p for x in h]
        l = list(range(n))
        l.sort(key=cmp)
        cur = sum(d)
        ret = 0
        for i in l:
            ret += cur * h[i]
            cur -= d[i]
        return ret