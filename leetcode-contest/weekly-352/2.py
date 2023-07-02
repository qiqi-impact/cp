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
    def findPrimePairs(self, n: int) -> List[List[int]]:
        PRIMES = get_primes(n)
        SP = set(PRIMES)

        ret = []
        for p in PRIMES:
            if n < p*2:
                break
            elif n-p in SP:
                ret.append((p, n-p))
        return ret