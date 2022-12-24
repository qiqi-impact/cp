class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def f(x):
            if x == 1:
                return 0
            if x%2:
                return 1 + f(3*x+1)
            else:
                return 1 + f(x//2)
        l = list(range(lo, hi+1))
        l.sort(key=lambda x:(f(x), x))
        return l[k-1]