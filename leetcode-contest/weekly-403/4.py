class Solution:
    def minimumSum(self, g: List[List[int]]) -> int:
        @cache
        def one(a, b, c, d):
            ar, br, ac, bc = inf, -inf, inf, -inf
            for i in range(a, b+1):
                for j in range(c, d+1):
                    if g[i][j]:
                        ar = min(ar, i)
                        br = max(br, i)
                        ac = min(ac, j)
                        bc = max(bc, j)
            if ar == inf:
                return 1
            return (br - ar + 1) * (bc - ac + 1)
        
        @cache
        def two(a, b, c, d):
            ret = inf
            for i in range(a, b):
                ret = min(ret, one(a, i, c, d) + one(i+1, b, c, d))
                ret = min(ret, one(a, i, c, d) + one(i+1, b, c, d))
            for i in range(c, d):
                ret = min(ret, one(a, b, c, i) + one(a, b, i+1, d))
                ret = min(ret, one(a, b, c, i) + one(a, b, i+1, d))
            return ret
        
        @cache
        def three(a, b, c, d):
            ret = inf
            for i in range(a, b):
                ret = min(ret, two(a, i, c, d) + one(i+1, b, c, d))
                ret = min(ret, one(a, i, c, d) + two(i+1, b, c, d))
            for i in range(c, d):
                ret = min(ret, two(a, b, c, i) + one(a, b, i+1, d))
                ret = min(ret, one(a, b, c, i) + two(a, b, i+1, d))
            return ret
        
        return three(0, len(g)-1, 0, len(g[0])-1)