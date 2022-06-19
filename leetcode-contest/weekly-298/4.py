class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        d = {}
        for x, y, z in prices:
            d[x,y] = max(d.get((x, y), 0), z)
        
        @cache
        def best(h, w):
            ret = 0
            if (h, w) in d:
                ret = d[h, w]
            for i in range(1, h//2 + 1):
                ret = max(ret, best(i, w) + best(h-i, w))
            for j in range(1, w//2 + 1):
                ret = max(ret, best(h, j) + best(h, w-j))
            return ret
        return best(m, n)