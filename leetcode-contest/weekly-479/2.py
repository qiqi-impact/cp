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

PRIMES = get_primes(500000)

class Solution:
    def largestPrime(self, n: int) -> int:
        lp = len(PRIMES)
        sp = set(PRIMES)
        ret = 0
        sm = 0
        for i in range(lp):
            sm += PRIMES[i]
            if sm <= n:
                if sm in sp:
                    ret = max(ret, sm)
            else:
                break
        return ret