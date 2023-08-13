from sortedcontainers import SortedList

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

PRIMES = get_primes(333)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        l = []
        for i, x in enumerate(nums):
            cur = 0
            for p in PRIMES:
                if x%p == 0: cur += 1
                while x%p == 0:
                    x //= p
                if p*p > x:
                    break
            if x != 1:
                cur += 1
            l.append((cur, i))
        l.sort(key=lambda x:(-x[0], x[1]))
        
        sl = SortedList([-1, len(nums)])
        
        amt = [None] * len(nums)
        
        for x, y in l:
            idx = sl.bisect_left(y)
            amt[y] = ((sl[idx] - y) * (y - sl[idx-1]), nums[y])
            sl.add(y)
        amt.sort(key=lambda x:-x[1])
        
        ret = 1
        for x, y in amt:
            c = min(k, x)
            k -= c
            ret *= pow(y, c, MOD)
            ret %= MOD
            if not k: break
        return ret