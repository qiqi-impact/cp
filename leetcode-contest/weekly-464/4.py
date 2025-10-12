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
PRIMES = get_primes(317)

class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        fac = []
        for x in nums:
            c = 0
            for p in PRIMES:
                m = 0
                while x % p == 0:
                    m += 1
                    x //= p
                if m % 2 != 0:
                    c ^= (1 << p)
            if x != 1:
                c ^= (1 << x)
            fac.append(c)
        # print(fac)
        
        ct = defaultdict(int)
        ret = 0
        def dfs(x, p):
            nonlocal ret
            ret += ct[fac[x]]
            ct[fac[x]] += 1
            for nei in g[x]:
                if nei != p:
                    dfs(nei, x)
            ct[fac[x]] -= 1
        dfs(0, -1)
        return ret
                
        