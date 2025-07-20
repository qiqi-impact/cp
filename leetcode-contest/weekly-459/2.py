MOD = 10**9+7
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        d = defaultdict(int)
        for x, y in points:
            d[y] += 1
        l = list(d.values())
        c2 = []
        for x in l:
            c2.append(x * (x - 1) // 2)
        ret = 0
        sm = 0
        for x in c2:
            ret += x * sm
            sm += x
            sm %= MOD
            ret %= MOD
        return ret