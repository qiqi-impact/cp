def get_primes(n):
    p = 3
    sieve = [1 for _ in range(n+1)]
    while p*p <= n:
        if sieve[p]:
            for x in range(p*p, n+1, 2*p):
                sieve[x] = 0
        p += 2
    ret = [2]
    for i in range(3, n+1, 2):
        if sieve[i]:
            ret.append(i)
    return ret

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9+7
        
        primes = get_primes(30)
        l = []
        for y in nums:
            cur = 0
            fail = False
            for i, x in enumerate(primes):
                if y % x == 0:
                    cur ^= (1 << i)
                if y % (x*x) == 0:
                    fail = True
                    break
            if not fail:
                l.append(cur)
        
        d = defaultdict(int)
        d[0] = 1
        for x in l:
            nd = defaultdict(int)
            for t in d:
                nd[t] += d[t]
                nd[t] %= MOD
                if t & x == 0:
                    nd[t^x] += d[t]
                    nd[t^x] %= MOD
            d = nd
        return (sum(d.values())-1+MOD)%MOD
        