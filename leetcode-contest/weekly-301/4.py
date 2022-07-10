primes = [2]
for i in range(3, 10**4, 2):
    pri = True
    for p in primes:
        if i%p == 0:
            pri = False
            break
    if pri:
        primes.append(i)

MOD = 10**9+7
N = 11111
comb = [[0 for _ in range(50)] for _ in range(N)]
comb[0][0] = 1
for i in range(1, N):
    for j in range(min(i+1, 50)):
        comb[i][j] = comb[i-1][j]
        if j > 0:
            comb[i][j] += comb[i-1][j-1]
        comb[i][j] %= MOD

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ret = 0
        for x in range(1, maxValue+1):
            xx = x
            v = 1
            for p in primes:
                ct = 0
                while xx%p == 0:
                    xx//=p
                    ct += 1
                v *= comb[n-1+ct][ct]
                v %= MOD
                if xx == 1:
                    break
            ret += v
            ret %= MOD
        return ret