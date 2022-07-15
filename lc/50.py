class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        neg = False
        if n < 0:
            neg = True
            n = abs(n)
        t = int(math.log(n)/math.log(2))
        p = [x]
        for i in range(t):
            p.append(p[-1] * p[-1])
        ret = 1
        for i in range(len(p)-1, -1, -1):
            if 1 & (n >> i):
                ret *= p[i]
        return 1/ret if neg else ret