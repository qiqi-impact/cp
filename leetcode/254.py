class Solution:
    def getFactors(self, n: int) -> List[List[int]]: 
        nn = n
        if n == 1:
            return []
        
        @cache
        def f(x, mn):
            ret = [[x]]
            for i in range(mn, x):
                if i*i > x:
                    break
                if x % i == 0:
                    l = f(x//i, i)
                    for e in l:
                        ret.append([i] + e)
            return ret
        
        r = set()
        for l in f(n, 2):
            if len(l) != 1:
                r.add(tuple(sorted(l)))
        return list(r)