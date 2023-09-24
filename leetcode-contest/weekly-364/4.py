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
PRIMES = set(get_primes(10**5))

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        
        g = [[] for _ in range(n+1)]
        
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        ret = 0
        def dfs(node, p):
            nonlocal ret
            v = int(node in PRIMES)
            cum = [0, 0]
            for ch in g[node]:
                if ch != p:
                    x, y = dfs(ch, node)
                    if v:
                        ret += cum[0] * x
                    else:
                        ret += cum[0] * y + cum[1] * x
                    cum[0] += x
                    cum[1] += y
            if v:
                ret += cum[0]
                return [0, cum[0]+1]
            else:
                ret += cum[1]
                return [cum[0]+1, cum[1]]
        dfs(1, -1)
        return ret