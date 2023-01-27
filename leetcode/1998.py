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
primes = get_primes(10**5)

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def find(x):
            if cc[x] != x:
                cc[x] = find(cc[x])
            return cc[x]
        def union(i, j):
            fi, fj = find(i), find(j)
            if fi != fj:
                cc[fi] = fj
        
        
        lp = len(primes)
        
        inv = {}
        for i, p in enumerate(primes):
            inv[p] = i
        
        cc = list(range(n+lp))
        
        for i, x in enumerate(nums):
            for j, p in enumerate(primes):
                while x%p == 0:
                    union(i, n+j)
                    x//=p
                if x == 1:
                    break
                if p*p > x and x > 1:
                    union(i, n+inv[x])
                    break
        
        roots = defaultdict(list)
        for i in range(n):
            roots[find(i)].append(nums[i])
        
        for k in roots:
            roots[k].sort(reverse=True)
    
        lst = -inf
        for i in range(n):
            cur = roots[find(i)].pop()
            if cur < lst:
                return False
            lst = cur
        return True
                    
                    