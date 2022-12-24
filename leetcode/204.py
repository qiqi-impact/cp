class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        ret = 1
        l = [True] * n
        for x in range(3, n, 2):
            if l[x]:
                ret += 1
                for y in range(x, n, x):
                    l[y] = False
        return ret