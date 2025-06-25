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

PRIMES = get_primes(1000)

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        ct = Counter(nums)
        s = set(PRIMES)
        for v in ct.values():
            if v in s:
                return True
        return False©leetcode