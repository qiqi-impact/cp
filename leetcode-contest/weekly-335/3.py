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
primes = get_primes(10**6)

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        d = {}
        for i, n in enumerate(nums):
            for p in primes:
                if p*p > n:
                    break
                while n%p == 0:
                    if p not in d:
                        d[p] = [i, i]
                    else:
                        d[p][1] = i
                    n//=p
            if n > 1:
                p = n
                if p not in d:
                    d[p] = [i, i]
                else:
                    d[p][1] = i
        st = [0] * (len(nums)+1)
        for l in d.values():
            st[l[0]] += 1
            st[l[1]] -= 1
        cur = 0
        for i in range(len(nums)-1):
            cur += st[i]
            if cur == 0:
                return i
        return -1