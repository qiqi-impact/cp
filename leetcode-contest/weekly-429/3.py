class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        s = [int(c) for c in s]
        n = len(s)
        ct = 0
        for i in range(n):
            if s[i] == i%2:
                ct += 1
        if min(ct, n - ct) <= numOps:
            return 1

        runs = [len(list(x[1])) for x in groupby(s)]

        def can(x):
            r = 0
            for b in runs:
                r += b // (x + 1)
                if r > numOps:
                    return False
            return True
        
        l, r = 2, n
        while l < r:
            mi = (l + r) // 2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r