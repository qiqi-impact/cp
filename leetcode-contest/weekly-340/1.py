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

PRIMES = set(get_primes(4 * (10**6) + 1))

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ret = 0
        for i in range(len(nums)):
            if nums[i][i] in PRIMES:
                ret = max(ret, nums[i][i])
            if nums[i][len(nums)-1-i] in PRIMES:
                ret = max(ret, nums[i][len(nums)-1-i])
        return ret